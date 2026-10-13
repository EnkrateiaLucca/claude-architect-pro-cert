# Lesson 0: The Exam Blueprint

**Exam domain:** all seven (how the exam is built) · **Time in session:** Segment 1, about 10 minutes

## What the exam asks

The official Exam Guide (v1.0, effective July 2026, exam code **CCAR-P**) describes the credential this way:

> "The Claude Certified Architect – Professional certification validates that an individual can design, build, and deliver production-grade AI solutions using Anthropic's Claude platform."

The guide lists seven things a credential holder can do:

- Design and prototype AI-driven solutions that address real business problems
- Select appropriate models, architectures, and API patterns for specific use cases
- Implement prompt engineering and context strategies to guide model behavior
- Integrate Claude into production systems using APIs, orchestration tools, and data pipelines
- Apply evaluation, monitoring, and observability practices to ensure solution quality
- Incorporate security, compliance, and governance considerations into system design
- Collaborate with cross-functional stakeholders and communicate architectural decisions effectively

Every item is written against one of **38 objectives** across seven domains. Lessons 1 to 7 quote each domain's objectives verbatim.

## Key ideas

### Logistics at a glance

| Item | Fact |
|---|---|
| Exam code | CCAR-P |
| Items | **63**, multiple-choice and multiple-response (each item states how many to pick) |
| Time | 120 minutes, about **1 min 54 s per item** |
| Passing score | Scaled **720** on a 100–1,000 scale. 720 is not 72% raw. |
| Score report | Pass/fail, scaled score, percent-correct by domain (domain scores do not decide pass/fail) |
| Fee | **$175** USD per attempt (partner-tier discounts apply at checkout) |
| Delivery | Pearson VUE, online proctored or test center |
| Prerequisites | **None.** Architect – Foundations is not required. |
| Recommended | 3+ years systems architecture, 6+ months hands-on with Claude or comparable LLMs in production |
| Validity | 12 months. On-time renewal is a free, non-proctored assessment. A lapsed credential means retaking the full exam. |
| Retakes | Wait 14 days after the 1st fail, 30 after the 2nd, 90 after the 3rd. Max 4 attempts per rolling 12 months. |
| Reschedule | Up to 24 hours before (guide). Changes inside 24 hours forfeit the fee. |
| Rules | Closed book, NDA before you start, no notes, no second monitor |

**Eligibility.** Registration goes through the Anthropic Partner Academy and currently requires a Claude Partner Network company email.

### The minimally qualified candidate (MQC)

> "an experienced practitioner who combines an engineering mindset with practical, real-world experience deploying AI solutions."

The MQC designs end-to-end systems (prompt and context engineering, RAG, API integration, orchestration, evaluation) and understands trade-offs in **cost, latency, performance, safety, and maintainability**. Those five words are the lens for every item. The guide excludes entry-level developers and people whose work is "limited to isolated tasks such as prompt writing without broader system design responsibility."

### The seven domains and their weights

| # | Domain | Weight | ~Items of 63 | Lesson |
|---|---|---|---|---|
| D1 | Solution Design & Architecture | 17% | ~11 | 01 |
| D2 | Claude Models, Prompting & Context Engineering | 13% | ~8 | 02 |
| **D3** | **Integration** | **19%** | **~12** | 03 |
| D4 | Evaluation, Testing & Optimization | 16% | ~10 | 04 |
| D5 | Governance, Safety & Risk Management | 14% | ~9 | 05 |
| D6 | Stakeholder Communication & Lifecycle Management | 14% | ~9 | 06 |
| D7 | Developer Productivity & Operational Enablement | 7% | ~4 | 07 |

Item counts are weight × 63, rounded. The guide publishes weights only. Three facts set your study priorities:

- **D3 Integration is the largest domain.** Least privilege, auth gaps, RAG, MCP vs. API vs. A2A, and observability.
- **D1 + D3 + D4 = 52%.** Design, integrate, and measure. That is the core of the exam.
- **D6 is 14%.** Stakeholder and lifecycle work counts as much as safety. Engineers who skip it lose about nine items.

### How items are written

The three official samples share one shape:

1. A production scenario with a concrete system (a support agent, a high-volume app, a RAG system).
2. A constraint or a **trigger** in the stem ("support staff only ever need to read tickets", "latency and cost are both concerns", "after a document refresh").
3. A question asking which change "best reduces risk", "most directly addresses both", or is "the most likely first place to investigate."
4. Four options. One fixes the root cause structurally. Three fail in predictable ways.

The correct answer is usually **the structural fix that matches the trigger and keeps the required capability.**

### The six distractor patterns

| Pattern | What it looks like | From the official samples |
|---|---|---|
| **Bigger model** | Upgrade or swap the model for a problem that is not about capability | "Replace the agent with a larger model that follows instructions more reliably." |
| **Watch, don't remove** | A detective or compensating control where a preventive one is available | "Add logging to the refund and delete tools." "Add a confirmation prompt." |
| **Prompt as policy** | Enforce a hard rule with instructions to the model instead of code, permissions, or config | "Tell the agent never to call the delete tool." |
| **Lossy shortcut** | Cut cost or latency by discarding something the task needs | "Truncate the policy document to the first 1,000 tokens." "Smallest model regardless of task fit." |
| **Wrong trigger** | A diagnosis that the event in the stem would not cause | "The model weights have silently changed." "The temperature is too low." |
| **Over-engineering** | Multi-agent, fine-tuning, or custom infrastructure where a workflow or one call suffices | "Split it into five specialized agents." |

*Prompt as policy* and *over-engineering* do not appear in the three samples. They are the two most common wrong answers in architect-level material (see `research/03-community-resources.md`), so learn them anyway.

### The core exam logic

Lessons 1 to 7 repeat these rules. They decide most items.

1. **Start with the simplest pattern that works.** Single call → workflow → agent → multi-agent, and only on evidence.
2. **Remove capability before you guard it.** Least privilege beats logging and confirmations.
3. **Enforce in code, not in the prompt.** Permissions, hooks, schemas, and validators hold. Instructions are best effort.
4. **Stable content first, then cache.** Order prompts static → dynamic and enable prompt caching.
5. **Diagnose from what changed.** Match the symptom to the trigger before touching the model.
6. **Measure before and after.** Every change ships with an eval, a metric, and a rollback.
7. **Design for the handoff.** Documentation, runbooks, and owners outlast the architect.

## Exam traps

- **Reading "best" as "most thorough."** The most elaborate option usually over-engineers.
- **Ignoring the trigger.** "After a document refresh", "only ever need to read", "every request repeats" decide the answer before you read the options.
- **Treating multiple-response items as partial credit.** No source confirms partial credit. Judge each option as its own true/false.
- **Skipping D6 and D7.** 21% of the exam is stakeholders, lifecycle, and team enablement.

## Exercise

Walk the three official samples in `exercises/00-official-samples.md`. Label each wrong option with one of the six patterns before you check the key.

## Check yourself

1. How many items does CCAR-P have, and how long do you have per item?
2. Which domain carries the most weight?
3. "Add a human confirmation step before the agent deletes accounts" when support staff never need deletion. Which pattern?

<details>
<summary>Answers</summary>

1. 63 items in 120 minutes, just under 2 minutes each.
2. D3 Integration at 19%.
3. Watch, don't remove. The role never needs deletion, so remove the tool.

</details>

## Official resources

- Exam Guide v1.0 (PDF): https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf
- Certifications overview: https://anthropic-partners.skilljar.com/page/partner-certifications
- Certifications FAQ: https://anthropic-partners.skilljar.com/page/faq-certifications
- Official prep path (5 courses): https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
- Pearson VUE for Anthropic: https://www.pearsonvue.com/us/en/anthropic.html
