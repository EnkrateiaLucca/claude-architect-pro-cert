# /// script
# requires-python = ">=3.11"
# dependencies = ["genanki>=0.13"]
# ///
"""Build practice artifacts from the two sources of truth.

questions/questions.json -> questions/practice-questions.md, questions/quiz.html
anki/flashcards.csv      -> anki/ccar-p-flashcards.apkg

Run: uv run build.py
"""
import csv
import html
import json
from collections import Counter
from pathlib import Path

import genanki

ROOT = Path(__file__).parent
DOMAINS = {
    "D1": ("Solution Design & Architecture", "17%"),
    "D2": ("Claude Models, Prompting & Context Engineering", "13%"),
    "D3": ("Integration", "19%"),
    "D4": ("Evaluation, Testing & Optimization", "16%"),
    "D5": ("Governance, Safety & Risk Management", "14%"),
    "D6": ("Stakeholder Communication & Lifecycle Management", "14%"),
    "D7": ("Developer Productivity & Operational Enablement", "7%"),
}


def check(qs):
    assert len(qs) == 60, f"expected 60 questions, got {len(qs)}"
    assert [q["id"] for q in qs] == list(range(1, 61)), "ids must run 1..60 in order"
    for q in qs:
        assert q["domain"] in DOMAINS, q["id"]
        assert set(q["answer"]) <= set(q["options"]), q["id"]
        assert len(q["answer"]) == q.get("select", 1), q["id"]
        assert set(q["wrong"]) == set(q["options"]) - set(q["answer"]), f"Q{q['id']} wrong-option notes"


def build_markdown(qs):
    counts = Counter(q["domain"] for q in qs)
    out = [
        "# Practice Questions: CCAR-P",
        "",
        "Sixty original, scenario-based questions in the style of the Claude Certified Architect – Professional exam. "
        "They are written for this course and are not drawn from the live exam, whose content is confidential.",
        "",
        "**How to use this bank**",
        "",
        "- **Timed run:** 60 questions in 114 minutes (1 min 54 s each, the real exam's pace). Open an answer only after you commit.",
        "- **Interactive:** open `quiz.html` in a browser for click-to-check practice with a score tracker and domain filter.",
        "- **Multiple-response items** say \"Choose TWO\". Score them all-or-nothing.",
        "- **Review every miss.** Write down which distractor pattern caught you (Lesson 00).",
        "",
        "| Domain | Weight | Questions |",
        "|---|---|---|",
    ]
    for d, (name, w) in DOMAINS.items():
        ids = [q["id"] for q in qs if q["domain"] == d]
        out.append(f"| {d} {name} | {w} | {counts[d]} (Q{ids[0]}–Q{ids[-1]}) |")
    out += [
        "",
        "**Distractor patterns** named in the explanations: *bigger model*, *watch, don't remove*, *prompt as policy*, "
        "*lossy shortcut*, *wrong trigger*, *over-engineering*.",
        "",
        "**Readiness bands** (rough guide, not calibrated to the scaled score): 52–60 strong, 45–51 close, "
        "36–44 keep studying your weakest domains, below 36 restart with the lessons.",
    ]
    current = None
    for q in qs:
        if q["domain"] != current:
            current = q["domain"]
            out += ["", "---", "", f"## {current}: {DOMAINS[current][0]}"]
        select = q.get("select", 1)
        stem = q["stem"] + (f" **(Choose {['', 'ONE', 'TWO', 'THREE'][select]}.)**" if select > 1 else "")
        out += ["", f"### Q{q['id']}", "", stem, ""]
        out += [f"- {k}. {v}" for k, v in q["options"].items()]
        ans = ", ".join(q["answer"])
        out += ["", "<details><summary>Answer</summary>", "", f"**Answer: {ans}**", "", f"**Why {ans} wins:** {q['why']}", ""]
        out += [f"- **{k} fails:** {v}" for k, v in q["wrong"].items()]
        out += ["", f"*Objective:* {q['objective']}", "", "</details>"]
    (ROOT / "questions" / "practice-questions.md").write_text("\n".join(out) + "\n")


QUIZ = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CCAR-P Practice Quiz</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>
:root{--cream:#f5f0e6;--paper:#fff;--ink:#1a1a1a;--muted:#6b6559;--line:#ddd5c0;--accent:#b85c1f;--ok:#4d8a3a;--bad:#c0392b;--okbg:#f2f7ef;--badbg:#fbefe4}
@media (prefers-color-scheme:dark){:root{--cream:#1c1c1c;--paper:#262626;--ink:#f5f0e6;--muted:#b8b2a4;--line:#3a3a3a;--okbg:#1f2e1b;--badbg:#3a2418}}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font:16px/1.45 Inter,-apple-system,sans-serif}
header{position:sticky;top:0;background:var(--ink);color:var(--cream);padding:12px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;z-index:2}
header h1{font-size:18px;margin:0;font-weight:800}header .score{margin-left:auto;font-weight:700;color:#e7c548}
header select,header button{font:inherit;padding:4px 8px;border-radius:4px;border:0}
main{max-width:860px;margin:0 auto;padding:16px}
.q{background:var(--paper);border:2px solid var(--ink);padding:16px;margin:16px 0;border-radius:4px}
.meta{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700}
.stem{margin:8px 0 12px}
label{display:block;border:1px solid var(--line);padding:8px 10px;margin:6px 0;border-radius:4px;cursor:pointer}
label.right{background:var(--okbg);border-color:var(--ok)}label.wrong{background:var(--badbg);border-color:var(--bad)}
button.check{background:var(--ink);color:var(--cream);border:0;padding:8px 14px;font-weight:700;border-radius:4px;cursor:pointer}
.exp{display:none;margin-top:12px;border-top:2px solid var(--ok);padding-top:8px;font-size:15px}.exp.show{display:block}
.exp ul{padding-left:18px}.verdict{font-weight:800}
</style></head><body>
<header><h1>CCAR-P Practice Quiz</h1>
<select id="dom" aria-label="Filter by domain"><option value="">All domains</option>__DOMOPTS__</select>
<button id="reset">Reset</button><span class="score" id="score">0 / 0</span></header>
<main id="list"></main>
<script>
const QS = __DATA__;
const list = document.getElementById('list'), scoreEl = document.getElementById('score');
let done = {};
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function render(){
  const dom = document.getElementById('dom').value;
  list.innerHTML = '';
  QS.filter(q => !dom || q.domain === dom).forEach(q => {
    const multi = q.answer.length > 1, type = multi ? 'checkbox' : 'radio';
    const el = document.createElement('section'); el.className = 'q';
    el.innerHTML = `<div class="meta">Q${q.id} · ${q.domain}${multi ? ' · choose ' + q.answer.length : ''}</div>
      <div class="stem">${esc(q.stem)}</div>
      ${Object.entries(q.options).map(([k,v]) => `<label data-k="${k}"><input type="${type}" name="q${q.id}" value="${k}"> <b>${k}.</b> ${esc(v)}</label>`).join('')}
      <button class="check">Check</button>
      <div class="exp"><p class="verdict"></p><p><b>Why ${q.answer.join(', ')}:</b> ${esc(q.why)}</p>
      <ul>${Object.entries(q.wrong).map(([k,v]) => `<li><b>${k}:</b> ${esc(v)}</li>`).join('')}</ul></div>`;
    el.querySelector('.check').onclick = () => {
      const picked = [...el.querySelectorAll('input:checked')].map(i => i.value).sort();
      if (!picked.length) return;
      const ok = picked.join() === [...q.answer].sort().join();
      el.querySelectorAll('label').forEach(l => {
        const k = l.dataset.k;
        l.classList.toggle('right', q.answer.includes(k));
        l.classList.toggle('wrong', picked.includes(k) && !q.answer.includes(k));
      });
      const v = el.querySelector('.verdict'); v.textContent = ok ? 'Correct' : 'Not quite'; v.style.color = ok ? 'var(--ok)' : 'var(--bad)';
      el.querySelector('.exp').classList.add('show');
      done[q.id] = ok; tally();
    };
    list.appendChild(el);
  });
}
function tally(){const v=Object.values(done);scoreEl.textContent=v.filter(Boolean).length+' / '+v.length}
document.getElementById('dom').onchange = render;
document.getElementById('reset').onclick = () => { done = {}; tally(); render(); };
render();
</script></body></html>
"""


def build_quiz(qs):
    opts = "".join(f'<option value="{d}">{d} · {html.escape(n)}</option>' for d, (n, _) in DOMAINS.items())
    data = json.dumps(qs).replace("</", "<\\/")
    (ROOT / "questions" / "quiz.html").write_text(QUIZ.replace("__DOMOPTS__", opts).replace("__DATA__", data))


def build_anki():
    rows = list(csv.DictReader((ROOT / "anki" / "flashcards.csv").open()))
    assert len(rows) == 60, f"expected 60 flashcards, got {len(rows)}"
    model = genanki.Model(
        1607392319,
        "CCAR-P Flashcard",
        fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Domain"}],
        templates=[{
            "name": "Card",
            "qfmt": '<div class="dom">{{Domain}}</div><div class="front">{{Front}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>',
        }],
        css=".card{font-family:Inter,-apple-system,sans-serif;font-size:19px;text-align:left;color:#1a1a1a;background:#f5f0e6;padding:12px}"
            ".nightMode.card{color:#f5f0e6;background:#1c1c1c}"
            ".dom{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#b85c1f;font-weight:700;margin-bottom:8px}"
            ".front{font-weight:700}.back{line-height:1.45}",
    )
    deck = genanki.Deck(2059400110, "Claude Certified Architect – Professional (CCAR-P)")
    for i, r in enumerate(rows, 1):
        name = DOMAINS[r["domain"]][0]
        deck.add_note(genanki.Note(
            model=model,
            fields=[html.escape(r["front"]), html.escape(r["back"]).replace("\n", "<br>"), f"{r['domain']} · {html.escape(name)}"],
            tags=[f"CCAR-P::{r['domain']}"] + r["tags"].split(),
            guid=genanki.guid_for("ccar-p", i),
        ))
    genanki.Package(deck).write_to_file(ROOT / "anki" / "ccar-p-flashcards.apkg")


if __name__ == "__main__":
    qs = json.loads((ROOT / "questions" / "questions.json").read_text())
    check(qs)
    build_markdown(qs)
    build_quiz(qs)
    build_anki()
    print("built: questions/practice-questions.md, questions/quiz.html, anki/ccar-p-flashcards.apkg")
