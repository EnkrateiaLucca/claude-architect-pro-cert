# /// script
# requires-python = ">=3.11"
# dependencies = ["anthropic>=0.70"]
# ///
"""Exercise 2: watch prompt caching work, break it, then fix it.

Run: ANTHROPIC_API_KEY=... uv run exercises/scripts/prompt_caching.py
Cost: a few cents on the default model.
"""
import datetime

import anthropic

MODEL = "claude-haiku-5-5"  # any current model; minimum cacheable prefix is 512 tokens on current models

# A long, static policy block: the kind of prefix that repeats on every request.
POLICY = "\n".join(
    f"Policy {i}: Refunds for order class {i} are allowed within {14 + i} days of delivery when the item is "
    f"unused, in original packaging, and the customer provides the order number. Shipping fees for class {i} "
    f"are refundable only if the item arrived damaged or was the wrong item. Escalate disputes over ${100 * i} "
    f"to a human agent."
    for i in range(1, 41)
)
QUESTIONS = [
    "Can I return a class 3 item after 20 days?",
    "Is shipping refundable for a class 12 item that arrived late?",
    "Who handles a $2,500 dispute on class 20?",
]

client = anthropic.Anthropic()


def ask(system_blocks, question):
    r = client.messages.create(
        model=MODEL,
        max_tokens=150,
        system=system_blocks,
        messages=[{"role": "user", "content": question}],
    )
    u = r.usage
    print(f"  cache_write={u.cache_creation_input_tokens or 0:>6}  cache_read={u.cache_read_input_tokens or 0:>6}  uncached_input={u.input_tokens:>6}")


def now():
    return {"type": "text", "text": f"Current time: {datetime.datetime.now().isoformat()}"}


static = [{"type": "text", "text": POLICY, "cache_control": {"type": "ephemeral"}}]

print("1) Static prefix with a cache breakpoint: first call writes, the rest read")
for q in QUESTIONS:
    ask(static, q)

print("2) Timestamp BEFORE the policy: the prefix changes every call, so every call writes")
for q in QUESTIONS:
    ask([now(), *static], q)

print("3) Timestamp AFTER the cached block: the cache survives")
for q in QUESTIONS:
    ask([*static, now()], q)

print("\nTakeaway: order content static -> dynamic. Caching matches an exact prefix.")
