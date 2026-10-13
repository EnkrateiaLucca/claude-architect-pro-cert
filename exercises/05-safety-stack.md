# Exercise 5: Place the Safety Stack

**Lesson:** 05 · **Time:** 15 minutes · **Format:** design drill, then compare with the reference

## Scenario

A regional bank wants a **loan pre-qualification assistant** on its public website. Applicants chat with it. It can:

- answer product questions from the bank's rate sheet and FAQ (RAG)
- look up an applicant's existing accounts after login (`get_accounts` tool)
- submit a pre-qualification application to the loan system (`submit_prequal` tool)
- email a summary to the applicant (`send_email` tool)

Final credit decisions are made by underwriters. The bank operates in the EU and the US.

## Tasks

1. **Place five controls** on the request path: input screening, system prompt, tool-call authorization, output screening, audit. For each, name the check and whether it is model-based or deterministic.
2. **Decide fail behavior.** For each control, what happens when it errors or times out?
3. **Route review.** Which actions are automated, sampled, or require human approval? Use confidence, reversibility, and cost of error.
4. **Compliance map.** Fill a table: obligation → control → owner → evidence, for at least GDPR and one fairness obligation.
5. **Fairness.** Where could unequal outcomes arise, and how will you measure them?

<details><summary>Reference answer</summary>

**1–2. Controls and fail behavior**

| Layer | Check | Type | On failure |
|---|---|---|---|
| Input screening | Injection/jailbreak classifier (fast model), PII detector, off-topic filter | Model-based + regex | **Fail closed** for tool-using turns: answer only from FAQ, no tools, offer a human |
| System prompt | Scope (pre-qualification only, no credit decisions), say "I don't know", cite the rate sheet | Guidance | n/a (best effort, never the only control) |
| Tool authorization | `get_accounts` only for the authenticated user's own ID (from the session, never from model text); `submit_prequal` schema-validated; `send_email` only to the verified address on file | **Deterministic** | **Fail closed**: deny the call, log it |
| Output screening | No other customer's data, no promise of approval, rates match the current sheet, schema check on tool arguments | Deterministic + model-based judge | Hold the message and return a safe fallback |
| Audit | Inputs, retrieved chunks, tool calls, outputs, model/prompt versions | Deterministic | Alert; a gap in audit logging is an incident |

**3. Review routing**

- FAQ answers: automated, sampled weekly by compliance.
- `submit_prequal`: automated submission, but it is only a pre-qualification. **Underwriters decide.** Low-confidence extractions go to a human queue.
- `send_email`: automated to the verified address only. No free-form recipients.
- Any statement that sounds like a credit decision: blocked by output screening.

**4. Compliance map**

| Obligation | Control | Owner | Evidence |
|---|---|---|---|
| GDPR data minimization | Redact non-required PII before model calls; collect only pre-qual fields | Data protection officer | DPIA, data-flow diagram |
| GDPR residency / transfers | EU traffic processed in-region via the chosen cloud route | Platform lead | Provider configuration, DPA |
| GDPR rights on automated decisions | Underwriter makes the credit decision; applicant can reach a human | Head of lending | Process doc, HITL logs |
| Usage Policy high-risk (finance) | Human in the loop + AI disclosure in the chat UI | Product owner | UI screenshot, review logs |
| Fair lending (US) | Outcome monitoring by group; adverse-action explanations from underwriters | Model risk management | Monthly fairness report |

**5. Fairness**

Unequal outcomes can come from: the FAQ corpus answering better in one language, extraction errors that cluster on certain name formats or addresses, proxies (zip code) in pre-qual data, and reviewers treating AI-flagged cases differently. Measure: eval set with demographic and language variation, extraction accuracy by group, pre-qual pass rates by group in production, and reviewer override rates.

</details>
