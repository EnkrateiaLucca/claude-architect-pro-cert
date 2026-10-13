# /// script
# requires-python = ">=3.11"
# dependencies = ["anthropic>=0.70"]
# ///
"""Exercise 4: a tiny mixed-method eval harness.

- Task 1 (ticket classification) uses a code-based grader: exact match.
- Task 2 (summaries) uses an LLM judge with a rubric. Validate any judge against human labels before trusting it.

Run:        ANTHROPIC_API_KEY=... uv run exercises/scripts/eval_harness.py
Self-test:  uv run exercises/scripts/eval_harness.py --selftest   (offline, checks the graders)
"""
import re
import statistics
import sys
import time

BASELINE = "claude-sonnet-5-5"
CANDIDATE = "claude-haiku-5-5"  # change this, re-run, and decide whether the switch passes your gate
JUDGE = "claude-opus-5-5"  # a different, stronger model than the system under test
PRICE = {  # USD per million tokens (input, output); check the pricing page before relying on these
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-opus-5-5": (4.0, 20.0),
}
LABELS = ["billing", "shipping", "technical", "account"]

TICKETS = [
    ("I was charged twice for my March invoice.", "billing"),
    ("My package says delivered but nothing arrived.", "shipping"),
    ("The app crashes when I upload a PDF over 10MB.", "technical"),
    ("I can't log in after changing my email address.", "account"),
    ("Why did my subscription price go up this month?", "billing"),
    ("Tracking hasn't updated in 6 days.", "shipping"),
    ("Export to CSV gives me an empty file.", "technical"),
    ("Please delete my account and all my data.", "account"),
]
DOCS = [
    "Q3 revenue rose 8% to $4.2M, driven by enterprise renewals. Churn fell from 3.1% to 2.4%. "
    "Hiring paused in October; two engineering roles remain open.",
    "The outage on May 3 lasted 47 minutes. Root cause: an expired TLS certificate on the API gateway. "
    "Fix: automated renewal with alerting 30 days before expiry.",
]


def grade_label(output: str, expected: str) -> bool:
    """Code-based grader: first label word in the output must match exactly."""
    found = re.findall(r"\b(" + "|".join(LABELS) + r")\b", output.lower())
    return bool(found) and found[0] == expected


def parse_score(judge_output: str) -> int | None:
    m = re.search(r"<score>\s*([1-5])\s*</score>", judge_output)
    return int(m.group(1)) if m else None


def run(model, client):
    lat, cost, correct, scores = [], 0.0, 0, []

    def call(prompt, m=model, max_tokens=200):
        nonlocal cost
        t = time.perf_counter()
        r = client.messages.create(model=m, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}])
        if m == model:
            lat.append(time.perf_counter() - t)
            pin, pout = PRICE[m]
            cost += (r.usage.input_tokens * pin + r.usage.output_tokens * pout) / 1e6
        return "".join(b.text for b in r.content if b.type == "text")

    for text, label in TICKETS:
        out = call(f"Classify this support ticket as one of {LABELS}. Reply with the label only.\n\n<ticket>{text}</ticket>")
        correct += grade_label(out, label)

    for doc in DOCS:
        summary = call(f"Summarize in one sentence for an executive.\n\n<doc>{doc}</doc>")
        verdict = call(
            "Grade the summary for faithfulness to the source on a 1-5 scale.\n"
            "5 = every claim supported, key facts present. 1 = contains unsupported or wrong claims.\n"
            "Think briefly, then end with <score>N</score>.\n\n"
            f"<source>{doc}</source>\n<summary>{summary}</summary>",
            m=JUDGE, max_tokens=400,
        )
        if (s := parse_score(verdict)) is not None:
            scores.append(s)

    return {
        "accuracy": correct / len(TICKETS),
        "judge_mean": statistics.mean(scores) if scores else float("nan"),
        "p50_latency_s": statistics.median(lat),
        "cost_usd": cost,
    }


def selftest():
    assert grade_label("billing", "billing")
    assert grade_label("Label: Shipping.", "shipping")
    assert not grade_label("technical or account", "account")
    assert not grade_label("refund", "billing")
    assert parse_score("Reasoning... <score>4</score>") == 4
    assert parse_score("no score here") is None
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit()
    import anthropic

    client = anthropic.Anthropic()
    print(f"{'model':<20}{'accuracy':>10}{'judge':>8}{'p50 s':>8}{'cost $':>10}")
    for model in (BASELINE, CANDIDATE):
        r = run(model, client)
        print(f"{model:<20}{r['accuracy']:>10.0%}{r['judge_mean']:>8.2f}{r['p50_latency_s']:>8.2f}{r['cost_usd']:>10.4f}")
    print("\nEight tickets and two docs is a demo, not a decision. A real gate needs hundreds of cases.")
