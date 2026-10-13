# Exercise 3: Integration Design Review

**Lesson:** 03 · **Time:** 20 minutes · **Format:** find the problems, then compare with the reference

## Scenario: the proposed design

An enterprise wants an **internal IT and HR assistant** in Slack for 12,000 employees. The team's proposal:

1. One agent connected to **six MCP servers** (Jira, ServiceNow, Workday, Okta, Confluence, GitHub) exposing **47 tools**, all loaded into context on every request.
2. All servers authenticate with **one shared admin service account**. The agent passes the user's Slack name in the prompt "so it knows who is asking."
3. The system prompt says: "Only reset passwords for the person asking. Never show salary data to non-managers."
4. HR policies (1,800 pages, updated quarterly) are pasted into the system prompt.
5. Questions like "how many vacation days do I have left?" are answered from the policy documents.
6. A partner's benefits agent (built by another vendor on a different stack) will be called by **wrapping it as one more MCP tool that forwards the full conversation.**
7. Logging: the final answer only.

## Tasks

For each numbered item, name the problem, the exam objective it violates, and the fix.

<details><summary>Reference review</summary>

| # | Problem | Objective | Fix |
|---|---|---|---|
| 1 | **Capability bloat.** 47 tools degrade tool selection and burn context on every call | Evaluate tool/agent configuration for capability bloat; progressive discovery vs. monolithic context | Scope tools to the request type: route to IT or HR sub-agents with only the tools each needs. Load tools on demand (tool search / deferred loading, or Skills). Remove tools no workflow needs (e.g., GitHub write tools) |
| 2 | **Auth gap.** A shared admin account means every user acts as admin. The model "knowing" the user is not authorization | Analyze authentication and authorization requirements | Authenticate the user (SSO) and call downstream systems **on behalf of the user** with their own scoped token (OAuth delegation). Authorize in each server, never in the prompt. Never pass tokens through the model |
| 3 | **Prompt as policy.** Password-reset and salary rules live only in instructions | Implement guardrails; auth requirements | Enforce in code: the reset tool only accepts the authenticated user's ID from the session; Workday returns salary fields only for the user's direct reports |
| 4 | **Monolithic context.** 1,800 pages exceed a sensible prompt and change quarterly | Design a RAG pipeline; progressive discovery | RAG with structure-aware chunking (by policy section, keep headings), hybrid BM25 + embeddings, reranking, metadata (country, effective date). Re-index on each quarterly update and re-run evals |
| 5 | **Wrong retrieval for the data shape.** Vacation balance is live, per-person, structured data | Apply retrieval strategies matched to data shape and query pattern | Call Workday's balance API as a tool. Use RAG for the policy explanation only |
| 6 | **Wrong protocol.** Wrapping a peer agent as a tool and forwarding the whole conversation leaks data and ignores the other agent's lifecycle | Evaluate connection protocols (MCP, API/CLI, agent-to-agent) | Use an **agent-to-agent** protocol (A2A) with a defined task contract, or a plain API with a minimal payload. Send only the fields the task needs |
| 7 | **Observability gap.** Final-answer logs can't explain a bad tool call | Analyze observability challenges at scale | Trace every step: request ID, user, retrieved chunks, tool calls with arguments and results, model/prompt versions, tokens, latency. Redact PII. Sample traces for LLM-judge scoring |

**Accuracy-latency note:** routing to scoped sub-agents with fewer tools and a smaller model for simple IT lookups usually improves **both** accuracy and latency. Justify the configuration with eval numbers, not intuition.

</details>
