# Lesson 8: Exam Strategy and Study Plan

**Exam domain:** all · **Time in session:** Segment 5, about 10 minutes

## 1. Time budget

63 items in 120 minutes is **1 min 54 s per item**.

| Checkpoint | Target |
|---|---|
| Item 21 | 40 min elapsed |
| Item 42 | 80 min elapsed |
| Item 63 | 110 min elapsed, 10 min for flagged items |

Flag anything that takes more than 2.5 minutes, pick your best answer, and move on. Never leave an item blank.

## 2. How to read an item

1. **Read the last sentence first.** "Best reduces risk", "most directly addresses both", "first place to investigate" each want a different kind of answer.
2. **Find the trigger.** What changed? What does the role actually need? What constraint is non-negotiable (latency SLA, FedRAMP, budget)?
3. **Predict the answer** before reading the options.
4. **Label each option** with a distractor pattern. The survivor is usually right.

## 3. The six distractor patterns

| Pattern | Tell |
|---|---|
| **Bigger model** | "Switch to a more capable model" for a problem that is not about capability |
| **Watch, don't remove** | Logging, alerts, or confirmations where removing the capability is possible |
| **Prompt as policy** | "Add to the system prompt that..." for a rule that must always hold |
| **Lossy shortcut** | Truncate, drop, shrink, or "regardless of task fit" |
| **Wrong trigger** | A cause the event in the stem would not produce |
| **Over-engineering** | Multi-agent, fine-tuning, new infrastructure for a simple problem |

## 4. Cue words in the stem

| Cue | Points toward |
|---|---|
| "only ever need", "least privilege" | Remove tools or permissions |
| "must always", "never", "guarantee" | Deterministic enforcement (code, hooks, permissions, schema) |
| "same prompt on every request" | Prompt caching, static content first |
| "overnight", "not user-facing", "thousands of" | Message Batches API |
| "after a document refresh", "after re-indexing" | Retrieval / indexing |
| "after switching models" | Model mismatch or prompt tuned to the old model; re-run evals |
| "steps are known", "same every time" | Workflow, not agent |
| "can't reproduce", "only final answers logged" | Tracing |
| "live", "current status", "balance" | Tool call to the system of record |
| "part number", "error code", "ID" | Keyword/BM25 hybrid retrieval |
| "data warehouse", "totals by region" | Query tool |
| "across organizations", "another vendor's agent" | Agent-to-agent |
| "many clients", "Claude Desktop and Claude Code" | MCP server |
| "must run in our AWS account", "FedRAMP" | Cloud route decided by constraint first |
| "executive", "CFO", "approve" | Cost, risk, reversal, recommendation |
| "the architect is leaving" | Runbooks, eval suite, owners |
| "every developer", "no opt-out" | Managed settings |

## 5. Multiple-response items

Each item says how many to choose. Judge each option as an independent true/false statement. Treat the item as all-or-nothing: no source confirms partial credit.

## 6. Logistics

- Bring a valid, unexpired government photo ID that matches your registration exactly.
- Online proctoring: clear desk, single monitor, webcam on, no phone or watch.
- Reschedule or cancel at least 24 hours ahead (the exam guide). The FAQ and policies pages say 48 hours, so use **48 hours** to be safe.
- Retake waits: 14 days, then 30, then 90. Maximum 4 attempts in 12 months. Each attempt costs the full fee.
- Result appears at the end. Score report shows percent correct by domain.

## 7. Three-week study plan

Time follows the blueprint weights.

| Week | Focus | Do |
|---|---|---|
| 1 | D1 Solution Design (17%), D2 Models & Context (13%), D3 Integration (19%) | Lessons 01–03, exercises 00–03, run `prompt_caching.py`. Flashcards daily |
| 2 | D4 Evaluation (16%), D5 Governance (14%) | Lessons 04–05, exercises 04–05, run `eval_harness.py`. Q1–Q30 timed |
| 3 | D6 Stakeholders (14%), D7 Enablement (7%), full review | Lessons 06–08, exercises 06–07. Q31–Q60 timed, then all 60 again. Cheatsheet the night before |

Throughout: build and operate at least one small end-to-end Claude system with RAG, an eval suite, and logging. The exam guide recommends it, and nothing teaches the trade-offs faster.

## 8. Self-assessment

Rate yourself 1–3 on each statement. Anything at 1 goes to the top of your study list.

| Domain | I can... |
|---|---|
| D1 | Split work between Claude, systems, and humans; choose workflow vs. agent vs. multi-agent and state the cost |
| D2 | Pick a model by eval and cost per task; design a cacheable prompt; choose few-shot vs. CoT vs. structured outputs |
| D3 | Find capability bloat and auth gaps; design hybrid RAG; choose API vs. MCP vs. A2A; choose progressive vs. monolithic context |
| D4 | Write measurable criteria; design mixed-method evals; read an A/B result honestly; diagnose from the trigger |
| D5 | Place input, tool, and output controls that fail closed; route review by confidence, reversibility, cost; map obligations to controls |
| D6 | Run discovery; present cost, risk, reversal; define SLAs with breach responses; build a handoff package |
| D7 | Put each Claude Code setting at the right scope; choose guidance vs. enforcement; set up CI review |

## 9. Official resources

- Exam Guide v1.0 (PDF): https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf
- Certifications FAQ: https://anthropic-partners.skilljar.com/page/faq-certifications
- Pearson VUE for Anthropic: https://www.pearsonvue.com/us/en/anthropic.html
