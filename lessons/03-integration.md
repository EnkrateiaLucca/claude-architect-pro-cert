# Lesson 3: Integration

**Exam domain:** D3 (19%, ~12 items, the largest domain) · **Time in session:** Segment 2, about 20 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Evaluate tool/agent configuration for capability bloat
- Analyze authentication and authorization requirements to identify security gaps
- Evaluate accuracy-latency trade-offs and justify configuration decisions
- Analyze observability challenges and select monitoring strategies at scale
- Design a RAG pipeline with appropriate chunking and indexing strategies
- Apply retrieval strategies matched to data shape and query pattern
- Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)
- Evaluate progressive discovery vs. monolithic context strategy

Official Sample 1 sets the tone: when a support agent can issue refunds and delete accounts but staff only read tickets and draft replies, **remove the tools**. Logging, confirmations, and bigger models are the wrong answers.

## Key ideas

### Capability bloat

Every tool costs context, adds a selection decision, and widens the attack surface.

| Symptom | Fix |
|---|---|
| Agent picks the wrong tool | Fewer, clearer tools; consolidate overlapping ones; sharpen names and descriptions |
| Tool definitions eat context | **Tool search** with `defer_loading`: load rarely used tools on demand (it also preserves the prompt cache) |
| One agent serves many roles | Route to **scoped sub-agents**, each with only its tools |
| Tools the role never uses | **Remove them** (least privilege) |

### Authentication and authorization gaps

| Gap | Why it fails | Fix |
|---|---|---|
| Shared admin service account for all users | Every user acts as admin; no per-user audit | Per-user delegated tokens (OAuth) bound to the authenticated session |
| Identity taken from model text ("user_email" argument) | Injection or a lie changes who you are | Identity from SSO/session, authorization enforced server-side |
| MCP **token passthrough** | Breaks audience validation; confused-deputy risk | Server validates tokens issued **for it**; gets its own downstream credentials |
| Over-privileged credentials behind read-only tools | A compromised tool can do more than it exposes | Credentials scoped to exactly the exposed operations |
| API key in the browser or in a prompt | Key theft; prompt leakage | Backend proxy; secrets stay server-side |
| End users pass `file_id` values | Cross-tenant access | Never accept file IDs from users; one workspace per tenant for hard isolation |
| JIT provisioning only | Users are added at first login and **never removed** | SCIM, so removal in the IdP deprovisions |

### Accuracy-latency trade-offs

Levers, roughly in order of cost to try: prompt caching (cuts time to first token), fewer and better retrieved chunks with reranking, lower effort, a faster model for easy routes, parallel tool calls, streaming (perceived latency only), and for non-urgent volume the Batch API (slower, 50% cheaper). **Justify every choice with eval numbers** against the SLA and the accuracy floor.

### Observability and reliability at scale

Log per request: request ID, model, prompt version, tokens (including cache reads and writes), latency, `stop_reason`, tool calls with arguments and results, retrieved chunk IDs. Trace across agent steps with one correlation ID (OpenTelemetry). Redact PII before logging. Sample production traffic for LLM-judge scoring.

| Watch for | Why it's easy to miss |
|---|---|
| `stop_reason: "refusal"` | Arrives as **HTTP 200**. Error-rate dashboards never see it. Instrument refusals separately and configure fallback per request |
| 429 rate limit | Honor `retry-after`; ramp traffic gradually |
| 429 from a spend cap | No `retry-after`; retries keep failing. Alert, don't retry |
| 529 overloaded | Retry with backoff; fallback model or queue |
| Cache hit rate falling | Silent cost spike (Lesson 2) |

Reliability patterns the prep course names: **retries** with backoff (SDKs retry twice by default), **fallbacks** (another model, a cached answer, a human queue), and **circuit breakers** (stop calling a failing dependency).

Admin tooling: workspaces (per environment or tenant, with their own limits), the Usage & Cost Admin API, the Compliance API activity feed, and Claude Code's OpenTelemetry export.

### RAG pipeline design

Before building RAG: if the knowledge base is under about **200,000 tokens (~500 pages)**, put it all in the prompt with caching.

| Stage | Decision |
|---|---|
| **Chunking** | Structure-aware (by section and heading, keep tables and procedures whole) over fixed windows; some overlap |
| **Contextual retrieval** | Prepend 50–100 tokens of chunk-specific context before embedding and BM25 indexing. Anthropic measured retrieval failures down **35%** (contextual embeddings), **49%** (+ contextual BM25), **67%** (+ reranking) |
| **Indexing** | **Hybrid**: embeddings for meaning + BM25 for exact terms; metadata (source, date, region, permissions) for filters |
| **Retrieval** | Retrieve wide (top-20 beat top-5/10 in Anthropic's tests), **rerank**, pass the best to the model |
| **Generation** | Cite sources; allow "I don't know" |
| **Refresh** | Re-index on content change with the **same embedding model**; re-run retrieval evals (recall@k) after every refresh |

Official Sample 3: confident wrong answers right after a document refresh, with the model unchanged, point to the **retrieval/indexing step**.

### Retrieval matched to data shape and query pattern

| Data / query | Strategy |
|---|---|
| Unstructured docs, conceptual questions | Embeddings (hybrid) + rerank |
| IDs, part numbers, error codes, names | Keyword/BM25 + exact-match filters |
| Structured, aggregatable data ("Q3 sales by region") | Query tool (read-only SQL / API), not vectors |
| **Live state** (order status, balance, inventory) | Tool call to the system of record |
| Time- or permission-scoped content | Metadata filters (date, region, ACL) at retrieval time |
| Multi-hop questions | Agentic search: iterative queries |

### Connection protocols

| Mechanism | Choose when | Not when |
|---|---|---|
| **Direct API / CLI** | One consumer, deterministic call at a known step in code; CLIs coding agents already know | Many clients need to discover the capability |
| **MCP** (tools, resources, prompts) | One integration reused by many Claude clients (Desktop, Claude Code, custom agents); local via stdio, remote via Streamable HTTP with OAuth | A single fixed pipeline call |
| **Agent-to-agent (A2A)** | Independent agents, often across organizations, each owning tools, state, and policy, negotiating tasks | Something one agent can do with a tool |

The API's **MCP connector** supports tool calls only, needs a public remote server, and is not covered by Zero Data Retention. Use client-side SDK helpers for local servers.

### Progressive discovery vs. monolithic context

| | Monolithic | Progressive discovery |
|---|---|---|
| What | Load all tools/knowledge up front | Load an index; fetch details on demand (tool search, Skills, retrieval, file exploration) |
| Wins when | Small, static, always-needed context (cache it) | Large catalogs with sparse use per task |
| Costs | Context bloat, selection errors, attention dilution | Extra round trips; discovery can miss |

### Delivery routes

| Route | Fit | Watch |
|---|---|---|
| **Claude API** (Anthropic) | Full, newest feature set; `inference_geo: "us"` for US-only processing | Procurement may require a cloud route |
| **Claude Platform on AWS** | AWS billing with Anthropic operating inference | Check feature and ZDR terms |
| **Amazon Bedrock** | AWS-resident workloads, AWS commit, GovCloud (FedRAMP High) | Several features missing or delayed (e.g., Files API, Skills, MCP connector, Batches endpoint) |
| **Google Cloud Vertex AI** | GCP-resident workloads (FedRAMP High authorized) | Feature gaps similar to Bedrock; own deprecation dates |
| **Microsoft Foundry** | Azure customers | Some features need "Hosted on Anthropic" |

Constraints (procurement, residency, FedRAMP) rule routes out **before** latency and cost are compared.

## Exam traps

- **Watch, don't remove:** logging or confirmations instead of removing unneeded tools.
- **Prompt as policy:** "only access the current user's records" in the system prompt.
- **Vectors for everything:** live state, exact IDs, and aggregates each need a different retrieval strategy.
- **MCP for everything:** a single deterministic call is a plain API integration.
- **Final-answer logs only:** agent failures live in the intermediate steps.
- **Retrying a spend-cap 429** forever.

## Exercise

`exercises/03-integration-review.md`: review a 7-point integration design for an IT/HR assistant and fix every gap.

## Check yourself

1. Which retrieval strategy fits "what's the status of order 88123?"
2. A knowledge base is 120 pages and changes monthly. RAG or long context?
3. Name two reasons a remote MCP server should never forward the client's token to downstream APIs.

<details>
<summary>Answers</summary>

1. A tool call to the order system. It is live state, not a document.
2. Long context with prompt caching. 120 pages is well under ~200k tokens.
3. The downstream API can't verify the token was meant for it (audience), and the server becomes a confused deputy that bypasses its own controls and audit.

</details>

## Official resources

- Writing effective tools for agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- Tool search tool: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
- Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval
- MCP security best practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices
- MCP connector: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- Rate limits: https://platform.claude.com/docs/en/api/rate-limits · Errors: https://platform.claude.com/docs/en/api/errors
- Refusals and fallback: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
- Claude in Amazon Bedrock: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
- Official prep course 2, Enterprise Integration & Production: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
