# Anthropic Docs and Courses for the Claude Certified Architect – Professional (CCAR-P)

Research date: 2026-10-13. Sources are official Anthropic properties only (platform.claude.com, code.claude.com, anthropic.com, claude.com, support/privacy.claude.com, anthropic.skilljar.com, anthropic-partners.skilljar.com). Some pages were retrieved as raw markdown (`<page>.md`) or HTML and searched locally instead of summarized; the cited URL is the canonical page.

## Context

The CCAR-P exam tests whether an architect can pick the right surface, model, architecture, and control placement before code is written, then carry the system through production, governance, stakeholder approval, and team handoff. This file collects concrete, testable facts from Anthropic's own material, grouped by the five lessons of the official Professional prep path. Facts are biased toward design decisions: "which option, when, and what does it cost or break."

## Exam overview (official exam guide)

- Exam code CCAR-P; guide Version 1.0, effective July 2026. [source: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf]
- 63 items, multiple-choice and multiple-response (each item states how many to select), 120 minutes, proctored (online or test center via Pearson VUE). [source: same exam guide PDF]
- Passing score: scaled 720 on a 100–1,000 scale; criterion-referenced; score report shows percent-correct by domain, which does not decide pass/fail. [source: same exam guide PDF]
- Fee $175 USD; credential valid 12 months; on-time renewal is a free, non-proctored assessment; a lapsed credential requires retaking the full exam at full fee. [source: same exam guide PDF]
- Retake waits: 14 days after first fail, 30 after second, 90 after third; max four attempts per rolling 12 months. Reschedule/cancel up to 24 hours before; later changes forfeit the fee. [source: same exam guide PDF]
- No mandatory prerequisites. Recommended: 3+ years systems architecture or platform engineering, 6+ months hands-on with Claude or comparable LLM systems in production. [source: same exam guide PDF]
- Domain weights: 1 Solution Design & Architecture 17%; 2 Claude Models, Prompting & Context Engineering 13%; 3 Integration 19%; 4 Evaluation, Testing & Optimization 16%; 5 Governance, Safety & Risk Management 14%; 6 Stakeholder Communication & Lifecycle Management 14%; 7 Developer Productivity & Operational Enablement 7%. [source: same exam guide PDF]
- Domain 3 objectives include "Evaluate tool/agent configuration for capability bloat", "Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)", and "Evaluate progressive discovery vs. monolithic context strategy". [source: same exam guide PDF]
- Domain 5 names GDPR, HIPAA, FedRAMP as example regulations; Domain 1 names architectural patterns "workflow, agentic, augmented LLM". [source: same exam guide PDF]
- Sample-question answer logic: least privilege means removing unneeded tools (not adding logging or confirmations); stable prefix first plus prompt caching addresses both latency and cost; confident-but-wrong answers after a document refresh point to retrieval/indexing first. [source: same exam guide PDF]
- Credly badge skills: AI Governance, Context engineering, Enterprise Architecture, Evaluation & optimization, Integration Architecture, Risk Management, Solution Design, Stakeholder Management; level "Intermediate". [source: https://www.credly.com/org/anthropic/badge/claude-certified-architect-professional]
- Prep path: "Claude Certified Architect - Professional Prep Course", 5 courses, free, described as "Learn to design, integrate, and govern production-grade Claude systems end to end, and to defend those design decisions to the stakeholders who fund and approve them." [source: https://anthropic-partners.skilljar.com/page/claude-certification-exam-prep-courses]
- Sibling certifications: Associate – Foundations ($99), Developer – Foundations ($125), Architect – Foundations ($125). [source: https://anthropic-partners.skilljar.com/page/partner-certifications]

### Prep-path lesson objectives (verbatim themes)

| Lesson | URL | Stated objectives (condensed) |
|---|---|---|
| 1 Claude Platform & Solution Design | https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/claude-platform-solution-design | Split work among Claude, existing systems, humans using "the four properties of generative AI"; choose augmented call vs workflow vs agent "by naming what each choice costs"; pick a reference architecture and "recognize when retrieval is doing a job that live-state should own"; use evals as the gate before any model swap; place entry points (Claude.ai, API, SDK, Claude Code, MCP server); rule out routes blocked by governance or regulated-industry constraints first. |
| 2 Enterprise Integration & Production | https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/enterprise-integration-production | Success criteria and eval suite before production code; model-based vs code-based evals; evals gate every change; POC-to-production checklist (cost/latency budget, retries, fallbacks, circuit breakers, failure modes); volume/token/cost estimation; SSO/OAuth, authorization, data handling, observability; A/B tests with hypothesis, metrics, sample size, "without overclaiming". |
| 3 Responsible AI, Safety & Risk | https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/responsible-ai-safety-risk-for-architects | What training reduces vs what the app layer must enforce; place input screening, output screening, tool-call authorization; model-based vs deterministic checks "so the system fails closed instead of failing open"; fairness/explanations; route review by confidence, reversibility, cost of a wrong answer; map each obligation to a control, owner, evidence artifact. |
| 4 Stakeholder Engagement, Lifecycle & GTM | https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm | Structured discovery to documented assumptions; present trade-offs as cost, risk, and "what a reversal would take"; lifecycle feedback loop (review triggers, SLA breach, iterate vs re-architect, governance checkpoints); partner GTM with Anthropic Applied AI team; compare direct API, Bedrock, Vertex, third-party routes on latency, compliance, cost; outcome document for a non-technical sponsor. |
| 5 Team Enablement & Operational Productivity | https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/developer-productivity-enablement | Shared configuration, rollout pattern, Skills distribution strategy, spend controls in team setup; review discipline for AI-generated work; connect symptoms to architecture causes; build team self-sufficiency. |

[source for all rows: the lesson URL in the row]

---

## Lesson 1: Claude Platform & Solution Design

### Findings: model lineup (as of 2026-10-13)

- Current models: Claude Fable 5.1 (`claude-fable-5-1`), Claude Opus 5.5 (`claude-opus-5-5`), Claude Sonnet 5.5 (`claude-sonnet-5-5`), Claude Haiku 5.5 (`claude-haiku-5-5`). Claude Mythos 5.1 has Fable 5.1's capabilities and is limited to orgs verified through programs such as the Cyber Verification Program. [source: https://platform.claude.com/docs/en/models/overview] [source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model]
- Official default: "If you're unsure which model to use, start with Claude Opus 5.5 for most workloads." Fable 5.1 is for "demanding reasoning and long-horizon agentic work", or when Opus 5.5 at higher effort still falls short on evals. [source: https://platform.claude.com/docs/en/models/overview]
- Positioning: Opus 5.5 "long-running agentic coding and knowledge work"; Sonnet 5.5 "best combination of speed and intelligence"; Haiku 5.5 "high-volume, latency-sensitive tasks such as classification, extraction, and routing". [source: https://platform.claude.com/docs/en/models/overview]
- All four current models: 1M-token context window, 128K max output (sync Messages API), reliable knowledge cutoff Jun 2026. Up to 300k output on Message Batches with beta header `output-300k-2026-03-24`. [source: https://platform.claude.com/docs/en/models/overview]
- List prices per MTok (input/output): Fable 5.1 $10/$50; Opus 5.5 $4/$20; Sonnet 5.5 $2/$10; Haiku 5.5 $0.10/$0.50 for prompts up to 100,000 tokens and $0.50/$2.50 above. Output is 5x input on every current model. [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Price ratios (derived from list prices): Fable 5.1 = 2.5x Opus 5.5 = 5x Sonnet 5.5. Haiku 5.5 short-prompt price is 1/20 of Sonnet 5.5. [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Long context: Claude 4.6+ models (except Haiku 5.5) bill the full 1M window at standard rates; "A 900k-token request is billed at the same per-token rate as a 9k-token request." [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Claude 4.7+ models use a newer tokenizer that "produces approximately 30% more tokens for the same text". [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Dateless IDs (4.6 generation onward) are pinned snapshots; pre-4.6 IDs carry a date and have aliases that point to the latest snapshot. Bedrock prefixes `anthropic.`; Opus 4.6 is the last Bedrock ID with `-v1`. [source: https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions]
- Legacy but available: Fable 5, Opus 5, Opus 4.8, 4.7, 4.6, 4.5, Sonnet 5, Sonnet 4.6, Haiku 4.5. [source: https://platform.claude.com/docs/en/models/overview]

### Findings: choosing a model, effort, thinking

- Two starting strategies: efficiency-first (start on Haiku 5.5, upgrade only for capability gaps) or capability-first (start on Opus 5.5, then lower effort or downgrade; move to Fable 5.1 if `xhigh`/`max` still fall short). [source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model]
- "Tuning effort is often a better lever than switching models." Creating use-case benchmark tests is "the most important step" in deciding whether to change models. [source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model]
- Effort levels: `low`, `medium`, `high`, `xhigh`, `max`, set via `output_config.effort`. Defaults: `medium` on Opus 5.5 and Haiku 5.5; `high` on Fable 5.1, Sonnet 5.5, and most others. Effort affects all output tokens (text, tool calls, thinking); "Effort is a behavioral signal, not a strict token budget." [source: https://platform.claude.com/docs/en/build-with-claude/effort]
- Changing top-level effort between requests invalidates prompt caching; per-message effort (beta header `mid-conversation-output-config-2026-07-01`) preserves the cache on 5.x models. [source: https://platform.claude.com/docs/en/build-with-claude/effort]
- Thinking: adaptive thinking is always on and cannot be disabled on Fable 5.1, Mythos 5.1, Fable 5, Opus 5.5; Sonnet 5.5 rejects `disabled` and offers `between_tools`; Haiku 5.5 accepts `disabled` at `high` or below. Manual extended thinking (`budget_tokens`) is deprecated on Opus 4.6/Sonnet 4.6 and not accepted on later models. [source: https://platform.claude.com/docs/en/build-with-claude/thinking] [source: https://platform.claude.com/docs/en/models/overview]
- Thinking tokens bill as output tokens and count toward `max_tokens` even when not returned. `display` defaults to `"omitted"` on current models; returned text is a summary, and "No `display` setting returns the raw chain of thought." [source: https://platform.claude.com/docs/en/build-with-claude/thinking]
- Fast mode (research preview): up to 2.5x higher output speed on Opus 5.5/Opus 5/Opus 4.8 at premium price ($8/$40 on Opus 5.5); Claude API first-party only; not available with Batch. [source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model] [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Breaking API constraints on newest models: forced tool use (`tool_choice` `any`/`tool`) returns 400 on Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1; assistant prefill returns 400 on Claude 4.6+ models. Use strict tool use or structured outputs instead. [source: https://platform.claude.com/docs/en/api/errors]
- Opus 5.5 rejects non-default `temperature`, `top_p`, `top_k`. [source: https://platform.claude.com/docs/en/models/opus-5-5/migration-guide]

### Findings: workflows vs agents (Building effective agents, Dec 19, 2024)

- Workflows: "LLMs and tools are orchestrated through predefined code paths". Agents: "LLMs dynamically direct their own processes and tool usage." [source: https://www.anthropic.com/engineering/building-effective-agents]
- "We recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all." Agentic systems "trade latency and cost for better task performance." [source: https://www.anthropic.com/engineering/building-effective-agents]
- Building block is "the augmented LLM": an LLM enhanced with retrieval, tools, and memory. [source: https://www.anthropic.com/engineering/building-effective-agents]
- Pattern selection rules: prompt chaining when a task decomposes into fixed subtasks (trades latency for accuracy); routing for distinct input categories; parallelization (sectioning or voting) for speed or confidence; orchestrator-workers when subtasks cannot be predicted; evaluator-optimizer when clear evaluation criteria exist and iteration measurably helps. [source: https://www.anthropic.com/engineering/building-effective-agents]
- Guardrails fit the sectioning pattern: one model instance handles the query while another screens it; this "tends to perform better than having the same LLM call handle both guardrails and the core response." [source: https://www.anthropic.com/engineering/building-effective-agents]
- Agents: higher cost and "potential for compounding errors"; recommend "extensive testing in sandboxed environments, along with the appropriate guardrails"; include stopping conditions such as a maximum iteration count. [source: https://www.anthropic.com/engineering/building-effective-agents]
- Three principles: simplicity, transparency (show planning steps), careful agent-computer interface (tool docs and testing). Frameworks can obscure prompts; start with direct API calls. The SWE-bench team spent more time on tools than on the overall prompt (absolute filepaths fixed relative-path errors). [source: https://www.anthropic.com/engineering/building-effective-agents]

### Findings: single vs multi-agent

- Anthropic's research system (Opus 4 lead, Sonnet 4 subagents) outperformed single-agent Opus 4 by 90.2% on its internal research eval. [source: https://www.anthropic.com/engineering/multi-agent-research-system]
- Token multipliers: agents use about 4x the tokens of chat; multi-agent systems about 15x. Token usage alone explained 80% of performance variance on the browsing eval. [source: https://www.anthropic.com/engineering/multi-agent-research-system]
- Poor fit for multi-agent: tasks where all agents need the same context, heavy inter-agent dependencies, most coding tasks, real-time coordination. [source: https://www.anthropic.com/engineering/multi-agent-research-system]
- Production lessons: start evals with about 20 real queries; LLM-as-judge with a single rubric prompt; human eval still needed; durable execution with resume; rainbow deployments to avoid breaking running agents; synchronous subagent execution is a bottleneck. [source: https://www.anthropic.com/engineering/multi-agent-research-system]
- Current docs frame multi-model cost strategies as Advisor (cheaper executor runs the loop and escalates to a frontier advisor; advisor tool is beta, runs server-side in one request) vs Orchestrator (frontier model holds the loop and delegates to cheaper workers via Managed Agents multiagent orchestration). [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]
- Orchestrator pays off mainly in two cases: capping the cost tail on routine work, and inputs larger than one context window. The documented Managed Agents limit used in benchmarks is 25 concurrent workers. [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]
- Advisor fails silently if the executor never consults it; executors "under-call" without a system prompt asking for consults. [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]

### Findings: RAG vs long context vs contextual retrieval vs context engineering

- "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt" (with prompt caching). [source: https://www.anthropic.com/news/contextual-retrieval]
- Contextual Retrieval prepends 50–100 tokens of chunk-specific context before embedding and BM25 indexing. Failure-rate reductions on top-20 retrieval: 35% (contextual embeddings), 49% (plus contextual BM25), 67% (plus reranking). Top-20 chunks beat top-10 or top-5. One-time cost with prompt caching: $1.02 per million document tokens. [source: https://www.anthropic.com/news/contextual-retrieval]
- Context engineering goal: "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome"; "context rot" degrades performance as context grows; prefer "just in time" retrieval or hybrid; long-horizon techniques are compaction, structured note-taking, and sub-agent architectures. [source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- Docs: "more context isn't automatically better"; up to 600 images or PDF pages per request (100 on 200k-window models). [source: https://platform.claude.com/docs/en/build-with-claude/context-windows]

### Findings: surfaces and when to use each

- Messages API: "Custom agent loops and fine-grained control." Claude Managed Agents: "Pre-built, configurable agent harness that runs in managed infrastructure", best for "Long-running tasks and asynchronous work". [source: https://platform.claude.com/docs/en/managed-agents/overview]
- Managed Agents concepts: Agent (model, prompt, tools, MCP servers, skills), Environment (Anthropic cloud sandbox or self-hosted sandbox), Session, Events. Beta header `managed-agents-2026-04-01`. Supports scheduled (cron) deployments. [source: https://platform.claude.com/docs/en/managed-agents/overview]
- Managed Agents is "not currently eligible for Zero Data Retention or HIPAA Business Associate Agreement (BAA) coverage" because sessions are stateful. [source: https://platform.claude.com/docs/en/managed-agents/overview]
- Managed Agents pricing: model token rates plus $0.08 per session-hour of `running` time; no batch discount; not available on partner-operated clouds. [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Agent SDK: Claude Code's tools, agent loop, and context management as a Python/TypeScript library "in a process you operate"; includes hooks, subagents, MCP, permissions, sessions, skills, plugins. Claude Code CLI is for interactive/one-off terminal work; Client SDK means you write the tool loop; Managed Agents means Anthropic hosts the loop. [source: https://code.claude.com/docs/en/agent-sdk/overview]
- Third-party products built on the Agent SDK may not offer claude.ai login or rate limits without approval, and may not brand as "Claude Code". [source: https://code.claude.com/docs/en/agent-sdk/overview]
- Claude Code provider recommendation for orgs: Claude for Teams/Enterprise is "the default recommendation"; Console for API-first or pay-as-you-go; Bedrock, Google Cloud's Agent Platform, or Foundry to inherit that cloud's compliance controls and billing. Cloud sessions, Routines, Code Review, Remote Control, and the Chrome extension need a claude.ai account. [source: https://code.claude.com/docs/en/admin-setup]

### Comparison: cloud delivery routes

| Route | Who operates inference | Billing | Notable gaps / facts |
|---|---|---|---|
| Claude API (1P) | Anthropic | Anthropic | Full feature set; `inference_geo` for US-only |
| Claude Platform on AWS | Anthropic (Anthropic is data processor) | AWS Marketplace, CCU at $0.01 | Same-day features, beta headers pass through, IAM/SigV4 or API key, ZDR on request |
| Amazon Bedrock | AWS ("zero operator access") | AWS | No structured outputs, Files API, code execution, web search/fetch, Agent Skills, MCP connector, Message Batches/Admin/Usage endpoints, Managed Agents, server-side fallback |
| Google Cloud (Agent Platform, formerly Vertex AI) | Google | Google | `model` in URL; `anthropic_version: vertex-2023-10-16` in body; 30 MB payload limit; no Files API, code execution, web fetch, Skills, MCP connector, Batches endpoint, Managed Agents, server-side fallback |
| Microsoft Foundry | Anthropic (Hosted on Azure or Hosted on Anthropic) | Azure Marketplace, CCU | Files API and Skills need "Hosted on Anthropic"; US Data Zone Standard = 1.1x |

[source: https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws] [source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock] [source: https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai] [source: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry] [source: https://platform.claude.com/docs/en/about-claude/pricing]

- Bedrock and Google Cloud regional/multi-region endpoints carry a 10% premium over global endpoints (Claude 4.5+ models). [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Prompt caches are isolated per workspace on Claude API, Platform on AWS, Foundry; per organization on Bedrock and Google Cloud. [source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching]

### Findings: platform features

**Prompt caching**
- Minimum cacheable length: 512 tokens on Fable 5.1, Mythos 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5; 1,024 on Opus 4.8, Sonnet 5, Sonnet 4.6/4.5; 2,048 on Opus 4.7; 4,096 on Opus 4.6/4.5 and Haiku 4.5. Shorter prompts silently do not cache. [source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching]
- Max 4 explicit breakpoints; lookback checks at most 20 positions per breakpoint; automatic caching via one top-level `cache_control`. [source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching]
- TTL: 5 minutes default (write 1.25x base input), 1 hour (`"ttl": "1h"`, write 2x). Reads 0.1x base on most models, 0.05x on Opus 5.5 and Sonnet 5.5, 0.025x on Fable 5.1 and Mythos 5.1. 5-minute writes break even after one read; 1-hour after two. [source: https://platform.claude.com/docs/en/about-claude/pricing]
- Invalidation hierarchy `tools` → `system` → `messages`: a tool-definition change invalidates everything; tool_choice or image changes invalidate system and messages caches. [source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching]
- Cached reads do not count toward ITPM rate limits on most models (Haiku 3.5 is the exception). [source: https://platform.claude.com/docs/en/api/rate-limits]
- Anthropic measured prompt caching as "the largest lever by a wide margin": 2.7x to 5.3x agent-loop cost reduction on its benchmarks. [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]

**Message Batches**
- 50% off input and output; most batches finish in under 1 hour; batches expire if not done in 24 hours (expired requests are not billed); results downloadable for 29 days; limit 100,000 requests or 256 MB per batch. [source: https://platform.claude.com/docs/en/build-with-claude/batch-processing]
- Recommend the 1-hour cache TTL for batches with shared context; batches can slightly exceed workspace spend limits. Batch processing is not ZDR-eligible. [source: https://platform.claude.com/docs/en/build-with-claude/batch-processing] [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]

**Structured outputs and citations**
- Structured outputs are GA: JSON outputs via `output_config.format` and strict tool use via `strict: true`. Unsupported schema features include recursive schemas, numeric/string length constraints, and `additionalProperties` other than `false`. Limits: 20 strict tools per request, 180-second grammar compile timeout. Compiled schemas are cached up to 24 hours. Refusals can break schema conformance. [source: https://platform.claude.com/docs/en/build-with-claude/structured-outputs]
- Citations and structured outputs are incompatible (400 error). `cited_text` does not count toward output tokens or later input tokens. All active models support citations. [source: https://platform.claude.com/docs/en/build-with-claude/citations]

**Files API**
- GA; 500 MB per file, 1 TB per organization; files are workspace-scoped; "Never accept `file_id` values from end users"; use a workspace per tenant for hard isolation (100 workspaces per org by default). Not ZDR-eligible. About 500 file requests per minute. [source: https://platform.claude.com/docs/en/build-with-claude/files]

**Context management**
- Context editing (beta header `context-management-2025-06-27`): tool-result clearing triggers by default at 100,000 input tokens and keeps the 3 most recent tool uses; clearing invalidates cached prefixes, so use `clear_at_least`. [source: https://platform.claude.com/docs/en/build-with-claude/context-editing]
- Compaction: server-side summary of older turns; on-demand (beta `compact-2026-09-04`, recommended where available) vs at a token threshold vs client-side summarizer. [source: https://platform.claude.com/docs/en/build-with-claude/compaction]
- Memory tool (`memory_20250818`): client-side; Claude requests file ops under `/memories` and your app executes them on storage you control; you must block path traversal (e.g. `/memories/../../secrets.env`). Pair with compaction so durable facts survive summarization. [source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool]

**Tools, MCP, Skills**
- Client tools run in your app (`stop_reason: "tool_use"`); server tools run on Anthropic infrastructure. [source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview]
- Tool use adds a hidden system prompt (286 tokens on Opus 5.5, Sonnet 5.5, Haiku 5.5 with `auto`). Web search costs $10 per 1,000 searches; web fetch has no extra charge; code execution has 1,550 free hours/month then $0.05 per container-hour, and is free when used with current web search/fetch versions. [source: https://platform.claude.com/docs/en/about-claude/pricing]
- MCP connector (beta `mcp-client-2025-11-20`): only MCP tool calls supported; server must be public over Streamable HTTP or SSE; local STDIO servers cannot connect directly. Not ZDR-eligible. Use client-side SDK helpers for local servers, prompts, or resources. [source: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector]
- Agent Skills use progressive disclosure: metadata ~100 tokens per skill always loaded; SKILL.md body under 5k tokens when triggered; bundled files cost nothing until read; script code never enters context, only output. [source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview]
- Skills on the API require the code execution tool, run with no network access and no runtime package installs; custom skills are workspace-wide on the API, per-user on claude.ai, filesystem-based (personal or project) in Claude Code; they do not sync across surfaces. Skills are not ZDR-covered. Use only trusted skills; audit them like installed software. [source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview]
- Skill `name`: max 64 chars, lowercase/numbers/hyphens, cannot contain "anthropic" or "claude"; `description` max 1024 chars and must state what and when. [source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview]

---

## Lesson 2: Enterprise Integration & Production

### Findings: rate limits, spend, errors

- Usage tiers are Start, Build, Scale (plus Custom). Monthly spend caps: Start $500, Build $1,000, Scale $200,000; Custom has no cap. [source: https://platform.claude.com/docs/en/api/rate-limits]
- Rate limits use a token bucket (continuous replenishment), measured as RPM, ITPM, OTPM per model class. A 429 includes `retry-after`. Sharp usage growth can trigger acceleration limits: "ramp up your traffic gradually". [source: https://platform.claude.com/docs/en/api/rate-limits]
- Example from docs: 2,000,000 ITPM with 80% cache hit rate lets you process 10,000,000 total input tokens per minute. [source: https://platform.claude.com/docs/en/api/rate-limits]
- Workspace limits: settable per limiter type; cannot be set on the Default Workspace; organization-wide limits always apply. A user-set spend limit returns HTTP 400 `invalid_request_error`; a tier spend-cap returns 429 with no `retry-after`, so retries keep failing. [source: https://platform.claude.com/docs/en/api/rate-limits] [source: https://platform.claude.com/docs/en/api/errors]
- Batch queue limits: Start 200,000, Build 300,000, Scale 500,000 batch requests in queue. [source: https://platform.claude.com/docs/en/api/rate-limits]
- Errors: 400 invalid_request, 401 authentication, 402 billing, 403 permission, 404 not_found, 409 conflict, 413 request_too_large, 429 rate_limit, 500 api_error, 504 timeout, 529 overloaded ("high traffic across all users"). Request size limits: 32 MB Messages, 256 MB Batch. [source: https://platform.claude.com/docs/en/api/errors]
- SDKs retry transient failures (connection errors, 429, 5xx) with exponential backoff, twice by default, honoring `retry-after`. Use streaming or Batches for requests that may exceed 10 minutes. Log `request-id` for support. [source: https://platform.claude.com/docs/en/api/errors]

### Findings: refusals and fallback (a reliability and safety control)

- Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5 include safety classifiers. A refusal is an HTTP 200 with `stop_reason: "refusal"` and `stop_details.category` (`cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, or null). [source: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback]
- Server-side fallback (beta, Claude API only): `fallbacks: "default"` retries on Anthropic's recommended model per category, or name up to three models. Not supported on Message Batches, Bedrock, Google Cloud, or Foundry (use SDK middleware there). Haiku 5.5 has no server-side fallback. [source: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback]
- Pre-output refusals in `bio`, `frontier_llm`, `reasoning_extraction` are billed (as of September 2026). Sticky routing remembers a fallback for about 1 hour, org-scoped, stored as a content hash. [source: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback]
- Pitfalls: retry on a different model; configure fallback on every request path; `fallbacks` does not propagate into sub-agent calls; "Make fallback a property of the request, not of ambient state... When you cannot confirm fallback is active, configure it rather than assume it is on"; instrument refusals separately because error-rate monitoring never sees an HTTP 200. [source: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback]

### Findings: cost and latency optimization

- "Free wins": prompt caching, token trimming, prompt audit, Batch at 50% for work that can wait 24 hours, workspace spend limits as backstop. "Tradeoffs": model choice, effort, output caps/task budgets, elapsed-time clock, multi-model architectures. [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]
- Compare models on cost per completed task, not per token. Running everything at low effort and re-running failures at `high` held pass rate at about half the cost on a measured coding benchmark. `max_tokens` of 64,000 covered all but 2 of 14,000 measured turns. [source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence]
- Pricing page guidance: Haiku for simple tasks, Sonnet for most production workloads, Opus for the most complex reasoning. [source: https://platform.claude.com/docs/en/about-claude/pricing]

### Findings: workspaces, identity, admin

- Every org has a Default Workspace that cannot be renamed, archived, or deleted; max 100 workspaces per org by default. Roles: Workspace User (playground only), Limited Developer, Developer, Admin, Billing (inherited). Org admins get Workspace Admin everywhere. [source: https://platform.claude.com/docs/en/manage-claude/workspaces]
- Files, Message Batches, and Skills are workspace-scoped; archiving a workspace archives its API keys and cannot be undone. A separate Claude Code workspace keeps Claude Code traffic apart from other API workloads. [source: https://platform.claude.com/docs/en/manage-claude/workspaces]
- Admin API credentials: Admin API key (`sk-ant-admin...`, provisioned only by admins), OAuth token with `org:admin`, or an unscoped personal/service-account key. Unavailable for individual accounts. [source: https://platform.claude.com/docs/en/manage-claude/admin-api]
- Usage & Cost Admin API supports cost reconciliation and alerting; Claude Code Analytics API reports sessions, lines added/removed, commits, PRs, tool acceptance rates, cost by model. [source: https://platform.claude.com/docs/en/manage-claude/usage-cost-api] [source: https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api]
- Compliance API gives Claude Enterprise and Console customers programmatic access to the Activity Feed (keys need `read:compliance_activities`). [source: https://platform.claude.com/docs/en/manage-claude/compliance-api]
- JIT provisioning: Team, Enterprise, Console; adds users at first login and never removes them. SCIM: Enterprise and Console only; IdP removal deprovisions automatically. Both require SSO setup with domain verification first. [source: https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning]
- SSO plan availability: the JIT/SCIM article lists "SSO: All plans" while the SSO search snippet lists Team, Enterprise, Console. [unverified]

### Findings: data retention, ZDR, HIPAA, residency

- ZDR: Anthropic does not store prompts or responses at rest after the response returns; enabled per organization via sales; each new org needs separate enablement. [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- ZDR does not cover: Claude Console/playground, Managed Agents, consumer plans, Team/Enterprise product interfaces (Claude Code on Enterprise has a separate ZDR offering), Claude for Excel, Covered Models, third-party integrations, and CORS (route browser calls through a backend proxy). [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- Covered Models (Fable 5.1, Mythos 5.1, Fable 5, Mythos 5) require 30-day retention; ZDR unavailable unless Anthropic authorizes it. [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- Even with ZDR or HIPAA, flagged content may be retained up to 2 years; legal requirements can also force retention. [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- ZDR feature eligibility: No for Batch, Files API, Agent Skills, code execution, programmatic tool calling, MCP connector, Managed Agents. Yes for prompt caching, memory tool, web search, web fetch, PDF, compaction. Structured outputs "Yes (qualified)" because schemas are cached up to 24 hours. Under ZDR the API does not block ineligible features; under HIPAA it returns 400. [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- HIPAA readiness: enable in Console with Anthropic's standard BAA; "the configuration is permanent and cannot be disabled"; not available on Claude Platform on AWS or Foundry; Claude Code not covered; do not put PHI in JSON schemas. [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention]
- Data residency: `inference_geo` = `"global"` (default) or `"us"`; US-only costs 1.1x on all token categories; supported on Claude 4.6+ only (older models return 400). Workspace geo is fixed at creation and `"us"` is the only option. Workspaces can enforce `allowed_inference_geos` and `default_inference_geo`. [source: https://platform.claude.com/docs/en/manage-claude/data-residency]
- Certifications listed: HIPAA-ready configuration (BAA), ISO 27001:2022, ISO/IEC 42001:2023, SOC 2 Type I and Type II, for Claude for Work and the Anthropic API. [source: https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained]

### Findings: Claude Code enterprise controls and security review

- Settings precedence (highest first): managed settings (file, MDM, or server-managed from claude.ai console) → command line `--settings` → `.claude/settings.local.json` → `.claude/settings.json` → `~/.claude/settings.json`. List keys such as `permissions.allow` merge across files. [source: https://code.claude.com/docs/en/settings]
- Managed file paths: macOS `/Library/Application Support/ClaudeCode/managed-settings.json`, Linux/WSL `/etc/claude-code/managed-settings.json`, Windows `C:\Program Files\ClaudeCode\managed-settings.json`. Server-managed settings are fetched at startup and polled hourly. [source: https://code.claude.com/docs/en/managed-settings]
- Managed-only lock keys include `allowManagedPermissionRulesOnly`, `allowManagedHooksOnly`, `allowManagedMcpServersOnly`, `blockedMarketplaces`, `disableSideloadFlags`, and `forceRemoteSettingsRefresh` (blocks startup until remote settings are fetched, exits if fetch fails: fail-closed). [source: https://code.claude.com/docs/en/managed-settings]
- Permission rules evaluate deny → ask → allow; "An allow rule can't carve an exception out of a deny rule." Modes: `default` (Manual), `acceptEdits`, `plan`, `auto` (classifier reviews actions), `dontAsk`, `bypassPermissions`. Disable risky modes with `permissions.disableBypassPermissionsMode` / `disableAutoMode`. [source: https://code.claude.com/docs/en/permissions]
- Enforcement menu for admins: permission rules, permission lockdown, sandboxing (`sandbox.enabled`, `sandbox.network.allowedDomains`), managed policy CLAUDE.md, MCP server allowlists, plugin marketplace control, hook restrictions, login enforcement, `allowedProviders`. [source: https://code.claude.com/docs/en/admin-setup]
- Security posture: Manual mode starts read-only; network commands like `curl`/`wget` are not auto-approved; unmatched commands require approval ("fail-closed matching"); credentials in macOS Keychain. Anthropic reviews directory connectors against listing criteria but "does not security-audit" them; prefer your own or trusted MCP servers. [source: https://code.claude.com/docs/en/security]
- Observability: OpenTelemetry export via `CLAUDE_CODE_ENABLE_TELEMETRY=1` plus OTLP exporters; prompt content, assistant responses, and tool content are not logged by default (`OTEL_LOG_USER_PROMPTS` etc. opt in). [source: https://code.claude.com/docs/en/monitoring-usage]
- Claude Code data: standard 30-day retention; 5 years for consumer users who allow training; local transcripts kept 30 days under `~/.claude/projects/` (`cleanupPeriodDays`); ZDR for Claude Code available to qualified Enterprise accounts. [source: https://code.claude.com/docs/en/data-usage]

---

## Lesson 3: Responsible AI, Safety & Risk for Architects

### Findings: Usage Policy (two versions in play)

- The anthropic.com Usage Policy page currently shows a version "Effective November 12, 2026". The previous version, effective September 15, 2025, remains in force until then. [source: https://www.anthropic.com/legal/aup] [source: https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944]
- Sept 2025 version: High-Risk Use Cases are Legal; Healthcare; Insurance; Finance; Employment and housing; Academic testing, accreditation and admissions; Media or professional journalistic content. Requirements: human-in-the-loop ("a qualified professional in that field must review the content or decision prior to dissemination or finalization") and disclosure of AI use "at a minimum at the beginning of each session". [source: https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944]
- Nov 2026 version: "High-risk AI Recommendations" span 11 areas: Legal, Medical, Finance, Credit, Insurance, Housing, Employment, Education and credentials, Healthcare access, Public benefits and services, Legal status and adjudication. A qualified person must "meaningfully review" the recommendation "with the authority to change or modify it" before delivery; recipients must be told AI was used, without needing to name Anthropic or Claude. [source: https://www.anthropic.com/legal/aup]
- Nov 2026 version adds "High-risk Physical Actions" (vehicles, force, hazardous energy, acting on the body, safety systems, industrial processes): a qualified individual must be able to stop the equipment, which must hold a safe state when connection to the service is lost. [source: https://www.anthropic.com/legal/aup]
- Nov 2026 exclusions: drafting/research/summaries that are not the delivered recommendation, and "wholly favorable" decisions (e.g., paying a claim) do not need HITL; partial approvals are not "wholly favorable". Law enforcement and criminal justice decisions are prohibited outright. [source: https://www.anthropic.com/legal/aup]
- Both versions: consumer-facing chatbots and external-facing agents must disclose users are talking to AI; agentic use must comply with the Usage Policy, and the Nov 2026 text makes users responsible for "actions those agents take through tools, browsers, or connected systems". [source: https://www.anthropic.com/legal/aup] [source: https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944]

### Findings: guardrails, jailbreaks, prompt injection

- Two threat models: jailbreaks/direct injection (the user is the adversary) and indirect injection (trusted user, adversarial third-party content in pages, emails, documents, tool results). [source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks]
- Direct-injection controls: harmlessness screen with Claude Haiku 5.5 plus structured outputs (treat a `refusal` from the screen as a harmful verdict), input validation, prompt engineering, throttling or banning repeat offenders. [source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks]
- Indirect-injection controls: put untrusted content only in `tool_result` blocks; label source and nature; state in the system prompt that tool content never overrides instructions; JSON-encode untrusted strings; never put your own instructions inside tool results; least privilege and sandboxing; screen tool outputs with a small classifier before returning them; red-team the agent; monitor continuously; chain safeguards. [source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks]
- Anthropic's browser-use defenses: RL training against injections, classifiers on untrusted content, human red teaming. Opus 4.5 reached a 1% attack success rate against adaptive attackers, still "meaningful risk"; "No browser agent is immune to prompt injection." [source: https://www.anthropic.com/research/prompt-injection-defenses]
- Constitutional Classifiers are input and output classifiers trained on synthetic data from a constitution. Jailbreak success fell from 86% to 4.4%; production refusal rate rose 0.38%; compute overhead 23.7%. [source: https://www.anthropic.com/research/constitutional-classifiers]
- Hallucination controls: allow "I don't know"; extract direct quotes first for documents over 20k tokens; verify each claim with a supporting quote or retract it; review summarized thinking; best-of-N consistency checks; iterative refinement; restrict to provided documents. [source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations]

### Findings: evaluation as a control

- Good success criteria are Specific, Measurable, Achievable, Relevant; most use cases need multidimensional criteria. [source: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests]
- Eval design: be task-specific (include edge cases), automate when possible, "Prioritize volume over quality". Grading preference: code-based (fastest, most reliable), then LLM-based (validate first, then scale), human grading last ("Avoid if possible"). LLM graders need detailed rubrics, constrained outputs, and thinking on. [source: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests]
- Agent evals: code-based graders are brittle to valid variations; model-based graders need calibration against humans. pass@k = at least one success in k tries; pass^k = all k succeed (75% per-trial over 3 trials ≈ 42%). Capability evals start at low pass rates; regression evals should sit near 100%. Start with 20–50 tasks from real failures; read the transcripts. [source: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents]

### Findings: RSP and ASL

- Responsible Scaling Policy version 3.4, effective July 8, 2026. ASL-3 Deployment Standard uses defense in depth with four layers: access controls, real-time prompt and completion classifiers, asynchronous monitoring classifiers, post-hoc jailbreak detection. The ASL-3 Security Standard lists 17 controls. [source: https://www.anthropic.com/responsible-scaling-policy]
- Capability thresholds named include CBRN uplift to "moderately resourced state programs" and AI R&D thresholds. [source: https://www.anthropic.com/responsible-scaling-policy]

### Findings: agent autonomy, oversight, audit

- Hooks give deterministic control; CLAUDE.md instructions are advisory. "Use hooks for actions that must happen every time with zero exceptions." [source: https://code.claude.com/docs/en/best-practices]
- Hook exit code 2 blocks the action; exit 0 on a `PreToolUse` hook "doesn't approve the tool call": the normal permission flow still applies. `ConfigChange` hooks can audit or block settings changes. [source: https://code.claude.com/docs/en/hooks-guide]
- Audit trails: Compliance API Activity Feed retained 6 years; Files API upload/download/delete appear in the Activity Feed only if the Compliance API was enabled first ("cannot be recovered later"). [source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention] [source: https://platform.claude.com/docs/en/build-with-claude/files]
- Claude Code cloud sessions run in isolated VMs; GitHub credentials never enter the VM; all operations are logged for audit. [source: https://code.claude.com/docs/en/security]
- Memory tool and Skills widen the attack surface: path traversal in memory handlers and malicious skills can exfiltrate data. [source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool] [source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview]

### Comparison: where each control sits

| Control | Placement | Type | Failure if missing or assumed |
|---|---|---|---|
| Haiku harmlessness screen | Before main call | Model-based | Direct jailbreaks reach the main model |
| Tool-output screen | Between tool and `tool_result` | Model-based | Indirect injection steers the agent |
| Strict tool use / structured outputs | Response contract | Deterministic | Schema drift breaks downstream parsing |
| Tool removal (least privilege) | Agent config | Deterministic | Successful injection can call destructive tools |
| Permission deny rules / hooks | Agent runtime | Deterministic | Advisory CLAUDE.md text gets ignored |
| Server-side fallback | Per request | Deterministic config | Refused requests fail silently as HTTP 200 |
| HITL review | Before delivery of high-risk output | Human | Usage Policy violation in high-risk areas |
| `forceRemoteSettingsRefresh` | Claude Code startup | Deterministic | Sessions run without org policy if fetch fails |

[source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks] [source: https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback] [source: https://code.claude.com/docs/en/managed-settings] [source: https://www.anthropic.com/legal/aup]

---

## Lesson 4: Stakeholder Engagement, Lifecycle & GTM

### Findings: use-case selection, pilots, ROI

- "Building trusted AI in the enterprise" uses four stages: Develop AI strategy, Create business value, Build for production, Deploy. [source: https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf]
- First use case criteria: well suited to LLM strengths (unstructured data, classification, format transformation); meaningful and measurable success metrics tied to business indicators; clear ROI; "Business critical, but low security risk." [source: https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf]
- Pilot advice: "Avoid the temptation, or external pressure, to tackle the biggest opportunities first"; look for enthusiastic sponsors, clear data availability, manageable compliance. [source: https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf]
- Graduation criteria to escape "pilot" limbo: performance thresholds (accuracy, latency, cost), operational readiness (stability, support, team capability), risk infrastructure (security compliance, data protection). [source: https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf]
- Governance: "Governance shouldn't be an afterthought. Establish an AI review board, define ethical guidelines, and create transparent processes for model evaluation and incident response." [source: https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf]
- Anthropic/Accenture pilot-to-production guide (Sept 14, 2026): seven considerations across before-pilot, pilot, production; four-part job definition (user, task, output, measurable quality threshold); four-tier oversight model (automated, sampled, reviewed, advisory); 42% of organizations have no single owner for AI costs and outcomes; 23% of C-suite leaders report sustained enterprise-wide impact. [source: https://claude.com/blog/deploying-ai-from-pilot-to-production]

### Findings: adoption evidence (Anthropic Economic Index)

- September 2025 report: 77% of business API uses show automation patterns vs about 50% for Claude.ai; nearly half of first-party API traffic is computer and mathematical tasks; a 1% increase in task cost index associates with only a 0.29% decrease in prevalence (weak price sensitivity); complex tasks "might be constrained more by access to information than on underlying model capabilities." [source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report]
- June 26, 2026 report ("Cadences"): median blog-producing chat/Cowork conversation has 13 rounds of back-and-forth vs a single human prompt in Claude Code; 93% of conversations produce an artifact. [source: https://www.anthropic.com/research/economic-index-june-2026-report]

### Findings: lifecycle, deprecation, migration

- Lifecycle states: Active, Legacy, Deprecated, Retired. Requests to retired models fail. At least 60 days' notice before retirement of publicly released models. [source: https://platform.claude.com/docs/en/about-claude/model-deprecations]
- Retirement dates apply to Anthropic-operated platforms (Claude API, Platform on AWS, Foundry). Bedrock and Google Cloud set their own lifecycle dates. [source: https://platform.claude.com/docs/en/about-claude/model-deprecations] [source: https://platform.claude.com/docs/en/models/overview]
- Find deprecated-model usage via Console Usage → Export CSV (by API key and model). [source: https://platform.claude.com/docs/en/about-claude/model-deprecations]
- Current retirement commitments: Opus 5.5 not sooner than Sept 22, 2027; Sonnet 5.5 not sooner than Sept 28, 2027; Haiku 5.5 not sooner than Oct 7, 2027; Fable 5.1 not sooner than Sept 1, 2027. Opus 4.1 retired Aug 5, 2026; Opus 4 retired June 15, 2026. [source: https://platform.claude.com/docs/en/about-claude/model-deprecations]
- Preservation commitment: weights of all publicly released models preserved "for, at minimum, the lifetime of Anthropic as a company"; retiring models are interviewed about their development and deployment. [source: https://www.anthropic.com/research/deprecation-commitments]
- Opus 5.5 migration checklist: change model ID; remove `thinking: disabled` and `budget_tokens`; set effort explicitly (default dropped from `high` to `medium`); replace forced `tool_choice`; handle `stop_reason: "refusal"` and configure fallback; re-baseline cost and latency; test in a development environment before switching production. [source: https://platform.claude.com/docs/en/models/opus-5-5/migration-guide]
- Choosing a model: evaluate with benchmark tests on actual prompts and data, compare accuracy, quality, edge cases, then weigh cost. [source: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model]

---

## Lesson 5: Team Enablement & Operational Productivity

### Findings: shared configuration

- CLAUDE.md scopes: managed policy (org-wide, "cannot be excluded by individual settings"), user `~/.claude/CLAUDE.md`, project `./CLAUDE.md` or `./.claude/CLAUDE.md` (commit it), local `./CLAUDE.local.md` (gitignore it). Claude Code can read `AGENTS.md` instead. [source: https://code.claude.com/docs/en/memory]
- Target under 200 lines per CLAUDE.md; use `.claude/rules/` for path-scoped rules; `@path` imports recurse to a maximum depth of four hops. Auto memory loads the first 200 lines or 25KB each session. [source: https://code.claude.com/docs/en/memory]
- Share team permissions, hooks, plugins, and env vars through committed `.claude/settings.json`; keep personal overrides in `.claude/settings.local.json`. [source: https://code.claude.com/docs/en/settings]

### Findings: Skills, plugins, subagents, hooks

- Claude Code skills live in `~/.claude/skills/` (personal) or `.claude/skills/` (project) and can be shared via plugins; claude.ai skills are per-user with no admin distribution. [source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview]
- A plugin packages skills, agents, hooks, and MCP servers as one unit, with a manifest at `.claude-plugin/plugin.json`, distributed through marketplaces. Use a plugin when you want several components installed and versioned together. [source: https://code.claude.com/docs/en/plugins]
- Admins restrict sources with `strictKnownMarketplaces` and `blockedMarketplaces`; "customization lockdown" can force skills, agents, hooks, and MCP servers to come only from plugins or managed settings. [source: https://code.claude.com/docs/en/admin-setup]
- Subagents run in their own context window with their own prompt, tool access, and permissions; use them to preserve context, enforce tool constraints, and cut cost by routing to models like Haiku. [source: https://code.claude.com/docs/en/sub-agents]
- A `SessionStart` hook with a `compact` matcher re-injects critical context after compaction. [source: https://code.claude.com/docs/en/hooks-guide]

### Findings: CI, review, and operations

- GitHub Actions: `/install-github-app` installs the Claude GitHub App, stores `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` as a repo secret, and opens a workflow PR; needs repo admin. For orgs, install the app once at org level and use an org-level Actions secret. The Action is built on the Agent SDK. [source: https://code.claude.com/docs/en/github-actions]
- Best practices: give Claude a way to verify its work; explore, then plan, then code; "Claude's context window fills up fast, and performance degrades as it fills." [source: https://code.claude.com/docs/en/best-practices]
- Cost baseline for budgeting: about $13 per developer per active day and $150–250 per developer per month across enterprise deployments; under $30 per active day for 90% of users. Pilot with a small group first. [source: https://code.claude.com/docs/en/costs]
- Usage visibility: OTel for all providers; analytics dashboard at claude.ai/analytics (Teams/Enterprise) or platform.claude.com/claude-code (Console); Claude Code Analytics API for Console. [source: https://code.claude.com/docs/en/admin-setup]
- Security habits for teams: audit `/permissions`, share approved permission configs through version control, enforce standards with managed settings, run `/security-review` on branch changes. [source: https://code.claude.com/docs/en/security]
- Anthropic docs reviewed here do not publish a runbook or handoff template for operational ownership. The prep lesson's objectives cover "building the team toward self-sufficiency". [unverified]

---

## Anthropic Academy courses relevant to an architect

| Course | URL | One-line summary |
|---|---|---|
| Building with the Claude API | https://anthropic.skilljar.com/claude-with-the-anthropic-api | "covers the full spectrum of working with Anthropic models using the Claude API" |
| Claude Platform 101 | https://anthropic.skilljar.com/claude-platform-101 | Building on the Claude Platform from the ground up |
| Introduction to Model Context Protocol | https://anthropic.skilljar.com/introduction-to-model-context-protocol | Build MCP servers and clients in Python; tools, resources, prompts |
| Model Context Protocol: Advanced Topics | https://anthropic.skilljar.com/model-context-protocol-advanced-topics | Sampling, notifications, file system access, transports for production MCP servers |
| Claude Code 101 | https://anthropic.skilljar.com/claude-code-101 | Using Claude Code in daily development |
| Claude Code in Action | https://anthropic.skilljar.com/claude-code-in-action | "Run long, hands-off Claude Code sessions you can trust: steer, configure, automate, and verify" |
| Introduction to agent skills | https://anthropic.skilljar.com/introduction-to-agent-skills | Build, configure, share Skills in Claude Code; distribute across teams |
| Introduction to subagents | https://anthropic.skilljar.com/introduction-to-subagents | Create subagents to manage context and delegate tasks |
| Claude with Amazon Bedrock | https://anthropic.skilljar.com/claude-in-amazon-bedrock | Course built for an AWS accreditation program |
| Claude on Google Cloud | https://anthropic.skilljar.com/claude-with-google-vertex | Working with Anthropic models on Google Cloud |
| Deploying Claude Enterprise with Confidence | https://anthropic.skilljar.com/deploying-claude-enterprise-with-confidence | Five rollout decisions: Structure & Identity, Access, Governance, Spend, Visibility |
| Introduction to Claude Cowork | https://anthropic.skilljar.com/introduction-to-claude-cowork | Cowork task loop, plugins and skills, steering multi-step work |
| AI Fluency for Builders | https://anthropic.skilljar.com/ai-fluency-for-builders | AI fluency for people owning problem-to-shipped-solution |
| AI Capabilities and Limitations | https://anthropic.skilljar.com/ai-capabilities-and-limitations | Introductory course on how AI works |

[source for all rows: https://anthropic.skilljar.com/]

Partner Academy Architect path also lists "deployment-architecture", "delivery-methodology", "product-foundations", and "claude-platform-model-foundations" courses (content not fetched). [source: https://anthropic-partners.skilljar.com/page/partner-certifications]

---

## Open questions

- The exam guide is v1.0 (July 2026), and Opus 5.5, Sonnet 5.5, and Haiku 5.5 shipped later. Items may reference Opus 5/Sonnet 5-era defaults (e.g., `high` effort default). Decide whether course material teaches current or exam-era defaults, or both.
- The Usage Policy changes on Nov 12, 2026. Decide which version the course teaches; the high-risk area list and HITL wording differ.
- "The four properties of generative AI" (AI Fluency Foundations) underpin lessons 1 and 2. Their exact definitions were not fetched. [unverified]
- Prep-course lesson bodies sit behind free registration. Only public objectives were captured.
- The Trust Center (trust.anthropic.com) renders client-side and returned no content; certification facts come from the privacy.claude.com article instead. FedRAMP status was not verified. [unverified]
- Claude Enterprise plan specifics (seat minimums, plan context limits) were not verified. [unverified]

## Fetch log

- Failed: https://trust.anthropic.com/ (no server-rendered content).
- Not used: https://www.anthropic.com/economic-index (data panel shows "Loading data"); specific reports were cited instead.
- Redirect resolved: https://platform.claude.com/docs/en/agent-sdk/overview → https://code.claude.com/docs/en/agent-sdk/overview.
- WebFetch could not parse https://www-cdn.anthropic.com/e5c9de22bc8884089970bd262ca0c8b952cb9136.pdf; the PDF text was extracted locally with `pdftotext`.
