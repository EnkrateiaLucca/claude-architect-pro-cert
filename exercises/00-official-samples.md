# Exercise 0: Walk the Three Official Samples

**Lesson:** 00 · **Time:** 10 minutes · **Format:** read, label, check

The three items below are the official samples from Section 8 of the CCAR-P Exam Guide. Anthropic says they show "the style and cognitive level of the exam."

## Steps

For each sample:

1. Underline the **trigger** in the stem (the fact that decides the answer).
2. Label every option with one of the six distractor patterns from Lesson 00, or mark it as the fix: *bigger model*, *watch, don't remove*, *prompt as policy*, *lossy shortcut*, *wrong trigger*, *over-engineering*.
3. Pick the answer, then open the key.

## Sample 1 · D3 Integration

> A team exposes a customer-support agent that can read tickets, draft replies, issue refunds, and delete user accounts. Support staff only ever need to read tickets and draft replies. Applying least-privilege principles, which change best reduces risk?
>
> A. Add logging to the refund and delete tools so misuse can be audited later.
> B. Remove the refund and delete tools from the agent's configuration entirely.
> C. Keep all tools but add a confirmation prompt before refunds and deletions.
> D. Replace the agent with a larger model that follows instructions more reliably.

<details><summary>Key</summary>

**Trigger:** "only ever need to read tickets and draft replies."

**Answer: B.** Least privilege removes capabilities the role does not need. The attack surface disappears.

- A: *watch, don't remove*. Logging is a detective control. It records the damage after it happens.
- C: *watch, don't remove*. A confirmation is a compensating control. The capability is still there for a prompt injection to reach.
- D: *bigger model*. Model size does not change authorization scope.

</details>

## Sample 2 · D2 Models, Prompting & Context

> An application sends the same 8,000-token system prompt and policy document on every request, followed by a short, varying user message. Latency and cost are both concerns. Which optimization most directly addresses both?
>
> A. Truncate the policy document to the first 1,000 tokens.
> B. Switch to the smallest available model regardless of task fit.
> C. Place the static system prompt and policy before the dynamic content and enable prompt caching.
> D. Move the policy document into a few-shot example block.

<details><summary>Key</summary>

**Trigger:** "the same 8,000-token system prompt ... on every request" plus "latency and cost are both concerns."

**Answer: C.** A stable prefix plus prompt caching cuts both time-to-first-token and input cost. Nothing the task needs is discarded.

- A: *lossy shortcut*. The policy is required context.
- B: *lossy shortcut*. "Regardless of task fit" is the giveaway.
- D: wrong mechanism. Few-shot examples teach format. Relocating text does not create a reusable cached prefix.

</details>

## Sample 3 · D4 Evaluation & Optimization

> A RAG system suddenly returns confident but incorrect answers after a document refresh, while latency and model version are unchanged. What is the most likely first place to investigate?
>
> A. The model weights have silently changed.
> B. The retrieval/indexing step is returning irrelevant or stale chunks.
> C. The temperature setting is too low.
> D. The context window has shrunk.

<details><summary>Key</summary>

**Trigger:** "after a document refresh" with "model version unchanged."

**Answer: B.** The only thing that changed is the corpus. A broken re-index or mismatched embeddings feed the model poor context, and the model answers confidently from it.

- A: *wrong trigger*. The stem rules out a model change.
- C: *wrong trigger*. Low temperature makes output more deterministic. It does not cause wrong facts after a refresh.
- D: *wrong trigger*. Context windows do not shrink on their own.

</details>

## Debrief

All three samples reward the same move: find what the stem says changed or what the role needs, then pick the **structural** fix at that point. Monitoring, bigger models, and cheaper shortcuts are the reliable wrong answers.
