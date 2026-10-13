# Practice Questions: CCAR-P

Sixty original, scenario-based questions in the style of the Claude Certified Architect – Professional exam. They are written for this course and are not drawn from the live exam, whose content is confidential.

**How to use this bank**

- **Timed run:** 60 questions in 114 minutes (1 min 54 s each, the real exam's pace). Open an answer only after you commit.
- **Interactive:** open `quiz.html` in a browser for click-to-check practice with a score tracker and domain filter.
- **Multiple-response items** say "Choose TWO". Score them all-or-nothing.
- **Review every miss.** Write down which distractor pattern caught you (Lesson 00).

| Domain | Weight | Questions |
|---|---|---|
| D1 Solution Design & Architecture | 17% | 10 (Q1–Q10) |
| D2 Claude Models, Prompting & Context Engineering | 13% | 8 (Q11–Q18) |
| D3 Integration | 19% | 12 (Q19–Q30) |
| D4 Evaluation, Testing & Optimization | 16% | 10 (Q31–Q40) |
| D5 Governance, Safety & Risk Management | 14% | 8 (Q41–Q48) |
| D6 Stakeholder Communication & Lifecycle Management | 14% | 8 (Q49–Q56) |
| D7 Developer Productivity & Operational Enablement | 7% | 4 (Q57–Q60) |

**Distractor patterns** named in the explanations: *bigger model*, *watch, don't remove*, *prompt as policy*, *lossy shortcut*, *wrong trigger*, *over-engineering*.

**Readiness bands** (rough guide, not calibrated to the scaled score): 52–60 strong, 45–51 close, 36–44 keep studying your weakest domains, below 36 restart with the lessons.

---

## D1: Solution Design & Architecture

### Q1

A logistics company must process 25,000 bills of lading every night. Each document needs the same 14 fields extracted, checked against a carrier master table, and any mismatch sent to a clerk. The team proposes an autonomous agent with tools. Which architecture best fits?

- A. An autonomous agent that decides, per document, which extraction and validation steps to run and when to stop.
- B. A workflow: extraction with structured output, deterministic validation against the master table, mismatches routed to the clerk queue, run through the Message Batches API.
- C. A multi-agent system with one specialized subagent per field and an orchestrator that merges the 14 results.
- D. One call to the most capable model with the night's documents concatenated into a single long-context request.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** The steps are known in advance and identical for every document, so a workflow with predefined code paths fits. Deterministic validation belongs in code, and the Batch API suits non-urgent volume at 50% of the cost.

- **A fails:** Over-engineering. An agent adds latency, tokens, and unpredictability to a fixed sequence.
- **C fails:** Over-engineering. Fourteen subagents multiply tokens and coordination for a single extraction step.
- **D fails:** Lossy shortcut. 25,000 documents will not fit one context, and attention degrades long before the limit.

*Objective:* Select appropriate architectural patterns (workflow, agentic, augmented LLM)

</details>

### Q2

A research orchestrator spawns six subagents, one per market segment. The user told the orchestrator early on to exclude companies under $10M revenue and to report in a fixed table format. Subagent reports ignore both instructions. What is the most likely cause and fix?

- A. The subagents run on a smaller model. Upgrade every subagent to the orchestrator's model.
- B. The subagents hit their output limit. Raise max_tokens for each subagent call.
- C. Subagents do not inherit the orchestrator's conversation. Pass the exclusion rule and the output format explicitly in each subagent's task.
- D. Add a seventh subagent that filters out small companies and reformats the other reports afterward.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Each subagent starts with only the context it is given. Constraints the user stated to the orchestrator must be written into every delegated task.

- **A fails:** Bigger model. No model can follow an instruction it never received.
- **B fails:** Wrong trigger. Truncation would cut reports short; it would not drop specific rules.
- **D fails:** Watch, don't remove. A cleanup agent compensates for the missing context at extra cost instead of fixing it.

*Objective:* Design multi-agent systems and orchestration strategies

</details>

### Q3

For which task is an orchestrator-workers multi-agent design LEAST appropriate?

- A. Refactoring a module where every change depends on shared type definitions that other changes also edit.
- B. Surveying the public documentation of 30 independent vendors against the same criteria.
- C. Due diligence across eight unrelated data rooms, each summarized against a checklist.
- D. A breadth-first literature search across many sources whose total text exceeds one context window.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Tightly coupled work where every worker needs the same evolving context loses more to coordination than it gains from parallelism. A single agent fits better.

- **B fails:** Good fit: independent, parallel, breadth-first work.
- **C fails:** Good fit: independent partitions with a shared checklist.
- **D fails:** Good fit: the information exceeds one context window and splits cleanly.

*Objective:* Design multi-agent systems and orchestration strategies

</details>

### Q4

A wealth-management firm wants advisors to ask: 'What is client X's current allocation, and how does it compare with their stated risk profile?' Which division of work is best?

- A. Upload monthly statements to a long chat and let Claude compute current allocations from what it remembers.
- B. Fine-tune a model on all historical client statements so it knows each client's holdings.
- C. Load every client's portfolio into the system prompt each morning so Claude always has it.
- D. The portfolio system computes the current allocation through a tool call. Claude retrieves the risk profile and explains the comparison. The advisor owns any recommendation.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Exact, live figures belong to the system of record. Claude owns the language-shaped comparison. Humans own the consequential recommendation.

- **A fails:** Lossy shortcut. Statements go stale, and Claude should not own arithmetic on exact figures.
- **B fails:** Over-engineering. Fine-tuning does not keep live holdings current and is the wrong tool for facts.
- **C fails:** Lossy shortcut. A daily snapshot is stale for live state and wastes context on every client.

*Objective:* Translate business problems into Claude-based AI solutions

</details>

### Q5

A contract-review assistant launched three months ago. Quality has plateaued, and the team cannot say which failure types are most common. Reviewers fix outputs by hand in the document editor. What is the architecture missing?

- A. A model with a larger context window so whole contract families fit in one request.
- B. A feedback loop that captures reviewer corrections and overrides, labels them, adds them to the eval set, and drives prompt and retrieval changes.
- C. A second model that re-reviews every output before the human reviewer sees it.
- D. A longer, more detailed system prompt that lists every clause type the team has seen.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Without a loop from output back into evaluation, the team cannot measure failures or improve. Reviewer edits are free labeled data.

- **A fails:** Bigger model. Nothing points to context size as the cause.
- **C fails:** Over-engineering. It adds cost without telling anyone what fails.
- **D fails:** Prompt guesswork without measurement. It may help or hurt, and nobody would know.

*Objective:* Design end-to-end architectures (input → processing → output → feedback loops)

</details>

### Q6

A claims director says 'we want AI.' Discovery shows handlers spend 40% of their time summarizing medical records, and 30% of claims miss the 5-business-day decision SLA. Which value framing should anchor the design?

- A. Transformation, measured by the number of AI features shipped to the claims team this year.
- B. Cost, measured by keeping monthly model token spend under a fixed budget.
- C. Efficiency and performance SLA, measured by handler time per claim and the share of claims decided within 5 days.
- D. Productivity, measured by the number of prompts each handler runs per day.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** The pain is handler time and a missed SLA, so the pillars are efficiency and SLA performance, with metrics the director already reports.

- **A fails:** Feature count is an output, not business value.
- **B fails:** Token spend is a cost input. It says nothing about the claims problem.
- **D fails:** Prompt volume measures activity, not outcomes.

*Objective:* Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

</details>

### Q7

A single prompt reviews a 120-file pull request. Feedback on each file is shallow, and cross-file interface bugs are missed. Which decomposition is best?

- A. Per-file local analysis passes, then a separate cross-file integration pass focused on interfaces and data flow.
- B. A model with a larger context window so all 120 files and their history fit in one review call.
- C. Add 'be thorough and check cross-file issues' to the prompt and run the same review twice.
- D. Review only the 20 largest files, since most bugs concentrate in big changes.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Splitting into focused local passes plus an integration pass avoids diluting attention across 120 files and targets cross-file issues directly.

- **B fails:** Bigger model. More room does not fix attention spread across one giant prompt.
- **C fails:** Prompt emphasis does not change how attention is spent.
- **D fails:** Lossy shortcut. Small files can carry the breaking change.

*Objective:* Apply decomposition techniques for complex problem solving

</details>

### Q8

Which TWO signals justify an agent instead of a workflow? **(Choose TWO.)**

- A. The steps are identical for every input.
- B. The response must arrive in under one second.
- C. The number and order of steps depend on what is discovered along the way.
- D. The environment returns ground truth at each step (tool results, test runs) the model can use to course-correct.
- E. Auditors require a fixed, documented sequence of steps.

<details><summary>Answer</summary>

**Answer: C, D**

**Why C, D wins:** Agents fit open-ended problems where the path can't be predicted and the environment provides feedback at each step.

- **A fails:** Identical steps describe a workflow.
- **B fails:** Agent loops add latency, so a tight latency budget argues against them.
- **E fails:** A fixed audited sequence is a predefined code path, which is a workflow.

*Objective:* Select appropriate architectural patterns (workflow, agentic, augmented LLM)

</details>

### Q9

Campaign copy must be translated into nine languages to a detailed brand style guide with a scoring rubric. Quality matters more than speed. Which pattern fits best?

- A. Routing, sending each language to a different model tier based on how common the language is.
- B. Evaluator-optimizer, with languages processed in parallel: one call translates, another scores against the rubric and requests revisions.
- C. An autonomous agent that researches each market and decides how to translate the copy.
- D. One zero-shot call per language to the most capable model, shipped without review.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Clear evaluation criteria plus measurable gains from iteration is the textbook case for evaluator-optimizer. Independent languages parallelize.

- **A fails:** Routing addresses varied input types, not quality refinement against a rubric.
- **C fails:** Over-engineering. The steps are known.
- **D fails:** Bigger model. It skips the rubric check that quality depends on.

*Objective:* Select appropriate architectural patterns (workflow, agentic, augmented LLM)

</details>

### Q10

Contact-center agents want suggested answers during live calls, built from a product knowledge base and the caller's current order status, within 2 seconds. Which design fits?

- A. One augmented-LLM call: retrieval over the knowledge base plus an order-status tool, a fast model, a cached system prompt, and streaming.
- B. A multi-agent research system that investigates each question across all internal sources before answering.
- C. A nightly batch job that pre-generates answers to the most likely questions for every open order.
- D. Retrieval over a nightly export of order data combined with the knowledge base in one index.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Augmenting a live interaction calls for the simplest pattern: one call with retrieval and a live tool, tuned for latency.

- **B fails:** Over-engineering. Multi-agent latency and cost break a 2-second budget.
- **C fails:** Pre-generated answers can't reflect the live call or current status.
- **D fails:** Retrieval is doing a job live state should own. Order status changes during the day.

*Objective:* Translate business problems into Claude-based AI solutions

</details>

---

## D2: Claude Models, Prompting & Context Engineering

### Q11

A triage system classifies 2 million tickets a month into 12 categories. The policy floor is 95% accuracy. On the eval set, the current large model scores 96.0%; a smaller model scores 95.6% at one-fifth the cost and three times the speed. What should the architect do?

- A. Keep the large model, since it is the most accurate option tested.
- B. Switch to the smaller model and retire the eval suite to save on evaluation costs.
- C. Switch to the smaller model, keep the eval suite as a CI gate, and route low-confidence tickets to the large model.
- D. Keep the large model and enable extended thinking to push accuracy higher.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** The smaller model clears the policy floor with large cost and latency gains. Evals stay as the gate, and routing handles the hard tail.

- **A fails:** Over-engineering. It pays five times the cost for 0.4 points nobody requires.
- **B fails:** Lossy shortcut. Removing the gate means the next regression ships unseen.
- **D fails:** Over-engineering. It adds cost and latency to an already compliant task.

*Objective:* Select appropriate Claude models based on trade-offs

</details>

### Q12

A legal drafting assistant sends a 40,000-token firm style guide and 30 examples before each user question, several times a minute. Time to first token is 6 seconds. Which change most reduces both latency and cost without losing quality?

- A. Move the user question to the start of the prompt so Claude reads it first.
- B. Keep the style guide and examples as an identical prefix on every request and place a cache breakpoint after them.
- C. Summarize the style guide down to 2,000 tokens and keep only five examples.
- D. Route all requests through the Message Batches API to get its 50% discount.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** A stable prefix plus prompt caching lets repeated content be read from cache, cutting time to first token and input cost while keeping all context.

- **A fails:** Putting dynamic content first breaks the cacheable prefix.
- **C fails:** Lossy shortcut. The guide and examples are what make the drafts right.
- **D fails:** Batch processing is asynchronous. It would make an interactive assistant slower.

*Objective:* Implement prompt reuse strategies (caching, modular prompts, Skills)

</details>

### Q13

An invoice extractor formats dates inconsistently and confuses 'ship date' with 'invoice date' on unusual layouts. Which first change is most effective?

- A. Add 'BE EXTREMELY CAREFUL WITH DATES' in capital letters to the instructions.
- B. Raise the temperature so the model explores alternative readings of each field.
- C. Switch to the most capable model and keep the prompt unchanged.
- D. Add three to five diverse examples covering unusual layouts with correct field mapping, and enforce the output format with a JSON schema.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Few-shot examples teach the mapping on hard layouts, and a schema fixes the format. Both target the observed failure.

- **A fails:** Emphasis is not information. The model still lacks examples of the confusing layouts.
- **B fails:** Wrong trigger. More randomness increases inconsistency.
- **C fails:** Bigger model. Try the cheap, targeted fix first and let evals decide.

*Objective:* Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)

</details>

### Q14

A financial-analysis feature answers multi-step questions. Final answers are often wrong, yet when the model shows its steps the logic is usually right and the arithmetic sometimes slips. What is the best fix?

- A. Enable extended thinking or step-by-step reasoning before the final answer, and send calculations to a code or calculator tool.
- B. Provide few-shot examples that show only final numeric answers for similar questions.
- C. Lower max_tokens so the model answers concisely without working through steps.
- D. Ask the model to state its confidence and suppress answers below 80%.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Reasoning before answering improves multi-step logic, and exact arithmetic belongs to a deterministic tool.

- **B fails:** Answer-only examples remove the reasoning that helps.
- **C fails:** Lossy shortcut. It suppresses the reasoning the task needs.
- **D fails:** Self-reported confidence is not calibrated, so it is a weak filter.

*Objective:* Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)

</details>

### Q15

A support agent handles cases that run 200+ turns with many large tool results. Late in a case it forgets constraints the customer stated early, and cost per case keeps rising. What is the best approach?

- A. Move to a model with a larger context window and keep the full transcript in every request.
- B. Delete the oldest half of the conversation whenever usage passes a threshold.
- C. Keep a structured case-facts block (constraints, decisions, IDs) at the top, clear stale tool results, and compact older turns into a summary.
- D. Restart the session every 20 turns with no carry-over to keep requests small.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Persisting critical facts outside the rolling history and trimming bulky, stale tool output keeps attention on what matters and controls cost.

- **A fails:** Bigger model. A longer window still buries early facts and raises cost.
- **B fails:** Lossy shortcut. It deletes exactly the early constraints that matter.
- **D fails:** Lossy shortcut. Restarting loses the case state.

*Objective:* Optimize context windows and manage token usage

</details>

### Q16

A bank is designing the system prompt for a customer chatbot. Which TWO items belong in the system prompt? **(Choose TWO.)**

- A. The rule that refunds over $200 need manager approval, enforced only through this instruction.
- B. Role, scope, and tone guidance for customer conversations.
- C. The customer's account number, so Claude can decide what they are authorized to see.
- D. An instruction to say it does not know when the knowledge base lacks the answer.
- E. The API key for the core banking system, so tools can authenticate.

<details><summary>Answer</summary>

**Answer: B, D**

**Why B, D wins:** System prompts carry role, scope, tone, and behavioral guidance such as admitting uncertainty. Hard rules, authorization, and secrets live outside the model.

- **A fails:** Prompt as policy. A refund limit must be enforced in the tool or a pre-tool check.
- **C fails:** Authorization must come from the authenticated session, not from text the model reads.
- **E fails:** Secrets never go into prompts. Tools authenticate server-side.

*Objective:* Design system prompts, templates, and guardrails

</details>

### Q17

Thirty teams each have procedural knowledge (brand rules, report templates, analysis scripts) that Claude should use across Claude apps and Claude Code. Loading all of it into every prompt wastes context. What is the best mechanism?

- A. Package each team's knowledge as an Agent Skill, so only its name and description load until the skill is needed.
- B. Concatenate all teams' material into one shared system prompt and cache it.
- C. Fine-tune a model per team on its templates and scripts.
- D. Ask users to paste the relevant documents into each conversation.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Skills use progressive disclosure: metadata sits in context, and instructions, scripts, and references load only when relevant. They are reusable across surfaces.

- **B fails:** Monolithic context. Caching lowers cost but every request still carries thirty teams' material.
- **C fails:** Over-engineering. Fine-tuning is costly and can't carry executable scripts or templates.
- **D fails:** Manual and inconsistent. It does not scale.

*Objective:* Implement prompt reuse strategies (caching, modular prompts, Skills)

</details>

### Q18

A Q&A feature puts the user's question first, followed by a 120,000-token contract. Answers miss details in the middle of the document. What should change first?

- A. Switch to the largest model available and keep the prompt layout.
- B. Split the contract into ten parts, ask the question of each, and concatenate the ten answers.
- C. Raise the temperature so the model samples more of the document.
- D. Place the contract first inside XML tags, put the question at the end, and ask Claude to quote the relevant passages before answering.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Anthropic's long-context guidance puts long documents at the top and the query at the end, and quote-then-answer focuses attention on the relevant text.

- **A fails:** Bigger model before a free layout fix.
- **B fails:** Lossy shortcut. Answers that span sections get fragmented.
- **C fails:** Wrong trigger. Temperature does not control attention.

*Objective:* Optimize context windows and manage token usage

</details>

---

## D3: Integration

### Q19

An internal agent connects to seven MCP servers exposing 52 tools. It picks the wrong tool 18% of the time, and tool definitions use about 30,000 tokens per request. What is the best change?

- A. Move to a more capable model that handles large tool catalogs better.
- B. Add 'choose tools carefully and read every description' to the system prompt.
- C. Scope each agent's tools to its task (route to sub-agents with small tool sets) and load rarely used tools on demand through tool search.
- D. Log every wrong tool selection and review the logs weekly with the team.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Capability bloat hurts selection accuracy and burns context. Fewer, task-scoped tools plus on-demand discovery fix both.

- **A fails:** Bigger model. The catalog itself is the problem.
- **B fails:** Prompt emphasis does not shrink the catalog or the token cost.
- **D fails:** Watch, don't remove. It measures the problem without fixing it.

*Objective:* Evaluate tool/agent configuration for capability bloat

</details>

### Q20

A CRM MCP server authenticates with one service account. The agent passes a user_email argument, taken from what the user typed in chat, to decide whose records to return. What is the core gap and fix?

- A. Authorization rests on model-supplied identity. Authenticate users through SSO, call the CRM with a per-user delegated token bound to the session, and authorize server-side.
- B. Add to the system prompt that the agent must only access records belonging to the current user.
- C. Encrypt the user_email argument in transit between the agent and the MCP server.
- D. Log every CRM call with the user_email value for a monthly access review.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Identity must come from authentication, not from text the model can be talked into changing. The downstream system enforces access per user.

- **B fails:** Prompt as policy. A prompt injection or a lie in chat bypasses it.
- **C fails:** Transport encryption is irrelevant. The value itself is untrusted.
- **D fails:** Watch, don't remove. The breach still happens.

*Objective:* Analyze authentication and authorization requirements to identify security gaps

</details>

### Q21

Reviewing a remote MCP server design, which TWO findings are security gaps? **(Choose TWO.)**

- A. The server forwards whatever token the client sends straight to the downstream API (token passthrough).
- B. The server checks that each token was issued for it before using it.
- C. The server holds read-write admin credentials although it only exposes read-only tools.
- D. The server uses OAuth with PKCE to authorize users.
- E. Tool responses include only the fields each task needs.

<details><summary>Answer</summary>

**Answer: A, C**

**Why A, C wins:** Token passthrough breaks audience validation and enables confused-deputy attacks. Over-privileged credentials violate least privilege.

- **B fails:** Audience validation is a required control.
- **D fails:** OAuth with PKCE is the recommended authorization flow.
- **E fails:** Data minimization is good practice.

*Objective:* Analyze authentication and authorization requirements to identify security gaps

</details>

### Q22

A customer chat has a full-response p95 latency of 9 s against a 4 s SLA. Accuracy is 94% against a 90% target. It uses a large model at high effort and sends the top 20 retrieved chunks. Which approach best resolves this?

- A. Move the chat to the Message Batches API to cut cost and free capacity.
- B. Evaluate a faster model or lower effort, and reranked top-5 chunks, on the eval set. Adopt the configuration that meets 4 s with at least 90% accuracy.
- C. Remove retrieval so the model answers from its own knowledge more quickly.
- D. Turn on streaming and report the SLA as met based on time to first token.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** There is accuracy headroom to trade for latency. Candidate configurations are compared on the eval set and the decision is justified with numbers.

- **A fails:** Batch is asynchronous. It makes chat slower.
- **C fails:** Lossy shortcut. Accuracy would collapse below target.
- **D fails:** Streaming improves perceived latency only. The SLA is on the full response.

*Objective:* Evaluate accuracy-latency trade-offs and justify configuration decisions

</details>

### Q23

A multi-agent system in production gives occasional wrong answers that the team cannot reproduce. Logs capture only the final answer. Which monitoring strategy fits?

- A. Keep final-answer logs for two years instead of 30 days so more examples accumulate.
- B. Upgrade every agent to a more capable model to reduce the error rate.
- C. Add a feedback button and investigate only conversations users report.
- D. Distributed tracing with one request ID across orchestrator and subagents, capturing prompt versions, retrieved context, tool calls and results, tokens, and latency, with PII redacted and sampled traces scored by an LLM judge.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Agent failures happen in intermediate steps. End-to-end traces make them reproducible and measurable at scale.

- **A fails:** More of the same logs still hide the steps that failed.
- **B fails:** Bigger model without a diagnosis.
- **C fails:** Users report a fraction of failures, and the traces still won't exist.

*Objective:* Analyze observability challenges and select monitoring strategies at scale

</details>

### Q24

A RAG system over equipment manuals uses fixed 500-token chunks. Tables and multi-step procedures are split mid-step, and answers skip steps. What is the best fix?

- A. Raise top-k from 5 to 50 so all pieces of a procedure are likely retrieved.
- B. Use a larger model that can infer the missing steps from partial chunks.
- C. Chunk on section and heading boundaries, keep tables and procedures intact, and store the heading path as metadata and chunk context.
- D. Shrink chunks to 100 tokens so retrieval is more precise.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Structure-aware chunking keeps semantic units together, and heading context improves retrieval and grounding.

- **A fails:** Lossy shortcut in reverse: it floods context with noise and cost without restoring order.
- **B fails:** Bigger model. It would guess missing steps, which is hallucination.
- **D fails:** Smaller chunks fragment procedures further.

*Objective:* Design a RAG pipeline with appropriate chunking and indexing strategies

</details>

### Q25

Technicians search with part numbers such as 'XR-7741-B' and error codes. Embedding-only retrieval returns similar but wrong parts. Which change fits the query pattern?

- A. Add keyword (BM25) retrieval in a hybrid setup with exact-match filters on identifiers, then rerank.
- B. Switch to a larger embedding model so identifiers are encoded more precisely.
- C. Increase chunk size so each chunk covers more part numbers.
- D. Instruct the model to double-check that part numbers match before answering.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Exact identifiers are a lexical match problem. Hybrid retrieval with keyword search and filters finds them; embeddings capture meaning, not exact strings.

- **B fails:** Bigger model. Semantic similarity still blurs near-identical codes.
- **C fails:** Larger chunks dilute relevance.
- **D fails:** Prompt as policy. The model can't verify what retrieval never returned.

*Objective:* Apply retrieval strategies matched to data shape and query pattern

</details>

### Q26

Managers ask questions like 'What were Q3 sales by region for product line X?' The data lives in a sales data warehouse. Which retrieval strategy fits?

- A. Embed every warehouse row in a vector database and retrieve the top-k most similar rows.
- B. Give Claude a read-only, parameterized query tool (or validated text-to-SQL) against the warehouse.
- C. Export the full warehouse into the context window on each request.
- D. Summarize the warehouse nightly into narrative documents and retrieve those with RAG.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Structured, aggregatable data calls for a query engine. Similarity search can't sum or group rows correctly.

- **A fails:** Vector similarity can't compute aggregates.
- **C fails:** Lossy and impossible at warehouse scale.
- **D fails:** Pre-summaries go stale and can't answer arbitrary slices.

*Objective:* Apply retrieval strategies matched to data shape and query pattern

</details>

### Q27

A fixed back-end pipeline calls one internal pricing service at a known step. No other client needs it. The team wants to wrap the service as an MCP server first. What do you recommend?

- A. Build the MCP server now so other teams can reuse it later.
- B. Use an agent-to-agent protocol so the pricing service can negotiate with the pipeline.
- C. Call the pricing API directly from the pipeline code.
- D. Package the pricing logic as an Agent Skill that Claude loads when needed.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** A deterministic call at a known step in code is a plain API integration. MCP pays off when many clients or models need to discover the capability.

- **A fails:** Over-engineering for a speculative future need.
- **B fails:** A2A is for independent agents, not a deterministic service call.
- **D fails:** Moves a deterministic step into model judgment for no benefit.

*Objective:* Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)

</details>

### Q28

A company wants its data platform usable from Claude Desktop, Claude Code, and three custom agents built by different teams. Which integration fits?

- A. Each team writes its own tool definitions and API wrapper inside its own app.
- B. An agent-to-agent protocol between every client and a new data-platform agent.
- C. Nightly CSV exports that each team uploads to its tool of choice.
- D. One remote MCP server with OAuth that exposes the platform's tools and resources to every MCP client.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** MCP standardizes one integration for many clients. Build it once and every MCP-capable host reuses it with consistent auth.

- **A fails:** Duplicated integrations drift and multiply security review.
- **B fails:** Over-engineering. No independent agent needs to negotiate here.
- **C fails:** Stale data and no access control.

*Objective:* Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)

</details>

### Q29

A supplier's inventory agent and a retailer's procurement agent, built by different companies on different stacks, must negotiate stock reservations. Each owns its tools, state, and policies. Which mechanism fits?

- A. An agent-to-agent protocol with a defined task contract between the two agents.
- B. Expose the supplier's inventory database to the retailer's agent through an MCP server.
- C. Merge both agents into one multi-agent system run by the retailer.
- D. Exchange emails between the companies and have Claude parse them on each side.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Independent agents across organizational boundaries need a peer protocol that keeps each side's tools and policies private.

- **B fails:** Hands another company direct data access and bypasses the supplier's own policies.
- **C fails:** Neither company will hand over its agent, data, and policies.
- **D fails:** Unstructured and unreliable for transactional commitments.

*Objective:* Evaluate connection protocols and select the appropriate integration mechanism (MCP, API/CLI, agent-to-agent)

</details>

### Q30

An agent can call any of 400 internal API endpoints. Loading every schema costs about 150,000 tokens per request, and most tasks touch three or four endpoints. Which strategy fits?

- A. Load all 400 schemas on every request and rely on prompt caching to absorb the cost.
- B. Progressive discovery: let the agent search or list endpoints and load only the schemas a task needs.
- C. Permanently cut the catalog to the 20 most-used endpoints.
- D. Switch to the model with the largest context window so all schemas fit comfortably.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** A large catalog with sparse use per task favors progressive discovery. Context stays small and selection stays accurate.

- **A fails:** Monolithic context. Caching helps cost, but attention and selection still suffer.
- **C fails:** Lossy shortcut. Real tasks need the long tail.
- **D fails:** Bigger model. It does not fix selection across 400 tools.

*Objective:* Evaluate progressive discovery vs. monolithic context strategy

</details>

---

## D4: Evaluation, Testing & Optimization

### Q31

Which success criterion for a document-summarization feature is best?

- A. Summaries should be good, accurate, and helpful for the business.
- B. Users should be satisfied with the summaries most of the time.
- C. At least 90% of summaries score 4 or higher on a faithfulness rubric validated against human graders, zero unsupported claims on a 200-case held-out set, p95 under 5 s, under $0.01 per summary.
- D. Summaries should use the most capable model available.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Criteria must be specific and measurable across accuracy, safety, latency, and cost.

- **A fails:** Not measurable.
- **B fails:** Vague and lagging. It can't gate a release.
- **D fails:** A design choice, not a success criterion.

*Objective:* Define evaluation metrics (accuracy, latency, cost, safety, security)

</details>

### Q32

A system classifies support tickets and drafts replies. Which TWO evaluation practices are sound? **(Choose TWO.)**

- A. Code-based exact-match grading for the category labels.
- B. The same prompt and model under test grade their own replies as the only judge.
- C. An LLM judge with a detailed rubric for reply accuracy and tone, validated against a human-graded sample.
- D. Testing only on 20 hand-picked tickets that the current prompt already handles well.
- E. Tuning prompts against the full dataset, including the held-out set.

<details><summary>Answer</summary>

**Answer: A, C**

**Why A, C wins:** Mixed methods: code grading where outputs are checkable, a validated LLM judge where they are nuanced.

- **B fails:** Self-grading shares the system's blind spots.
- **D fails:** Cherry-picked cases hide failures.
- **E fails:** Tuning on the held-out set leaks it and inflates scores.

*Objective:* Design evaluation datasets and test frameworks using mixed methodologies

</details>

### Q33

A new prompt variant scores 2.1 points higher on an LLM-judge metric across 60 conversations. Cost and latency are unchanged. The PM wants a global rollout today. What is best?

- A. Treat the result as inconclusive, estimate the sample size needed to detect a 2-point effect, run to that size with guardrail metrics, then decide.
- B. Roll out now; any measured improvement is worth shipping.
- C. Roll back; a 2-point difference is always noise for LLM outputs.
- D. Change three more prompt elements in the next test to find a bigger effect faster.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Sixty noisy samples can't support the claim. Size the test, watch guardrails, and don't overclaim.

- **B fails:** Overclaims a result that may be noise.
- **C fails:** Overclaims in the other direction. The effect may be real.
- **D fails:** Several simultaneous changes make the result unattributable.

*Objective:* Conduct A/B testing and iterative improvements

</details>

### Q34

After moving to a newer model version, a JSON extraction pipeline still returns valid JSON, but string fields now include extra commentary. Prompts and retrieval are unchanged. What is the most likely cause and first fix?

- A. The retrieval index went stale. Rebuild it and re-embed the corpus.
- B. Temperature is too low. Raise it to restore the old behavior.
- C. The context window shrank. Trim the input documents.
- D. The prompt was tuned to the old model's behavior. Re-run evals and tighten output constraints for the new model, for example a strict schema with structured outputs.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** The only change is the model. Newer models follow instructions differently, so re-evaluate and adapt the prompt and output constraints.

- **A fails:** Wrong trigger. Retrieval didn't change.
- **B fails:** Wrong trigger. Temperature doesn't add commentary.
- **C fails:** Wrong trigger. Context windows don't shrink.

*Objective:* Diagnose system issues (prompt failure, hallucinations, model mismatch)

</details>

### Q35

A policy Q&A bot sometimes invents clauses when the knowledge base lacks an answer. For those questions, retrieval returns only low-relevance chunks. What combination works best?

- A. Move to a more capable model that knows more policy language.
- B. Permit 'I don't know' when sources lack the answer, require citations to retrieved passages, and reject answers with claims the retrieved text doesn't support.
- C. Set temperature to 0 and ship.
- D. Add few-shot examples of confident, complete answers so the model stops hedging.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Grounding plus an explicit way out plus a support check targets fabrication when retrieval comes up empty.

- **A fails:** Bigger model. It invents more fluent clauses.
- **C fails:** Deterministic sampling still fabricates, just consistently.
- **D fails:** Teaches confidence, which worsens fabrication.

*Objective:* Diagnose system issues (prompt failure, hallucinations, model mismatch)

</details>

### Q36

After switching to a smaller model for cost, overall accuracy drops 2 points. All of the drop comes from multi-clause legal questions, 8% of traffic. Other categories are unchanged. What is best?

- A. Revert all traffic to the large model.
- B. Keep the small model for everything and accept the 2-point loss.
- C. Route the multi-clause category to the larger model and keep the small model for the rest, verified on the eval set.
- D. Add 'think harder on legal questions' to the prompt for all traffic.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** This is a model mismatch on one category. Routing keeps most of the savings and restores accuracy where it matters.

- **A fails:** Gives up the savings on the 92% that works.
- **B fails:** Accepts a known, fixable failure.
- **D fails:** Unmeasured prompt tweak instead of a targeted, testable fix.

*Objective:* Diagnose system issues (prompt failure, hallucinations, model mismatch)

</details>

### Q37

Every night, 50,000 product descriptions are generated with the same 6,000-token instructions. Nothing is user-facing until morning. What is the best cost optimization?

- A. Submit the jobs through the Message Batches API and cache the shared instructions.
- B. Use the real-time API with streaming so each description returns faster.
- C. Use the most capable model at high effort to avoid regeneration.
- D. Cut the instructions to 1,000 tokens to reduce input cost.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Non-urgent volume suits the Batch API's 50% discount, and caching cuts the repeated instruction cost further.

- **B fails:** Streaming helps perceived latency, which nobody needs overnight.
- **C fails:** Raises cost with no stated quality problem.
- **D fails:** Lossy shortcut. The instructions drive quality.

*Objective:* Optimize token usage, latency, and cost-performance trade-offs

</details>

### Q38

Which metric should guide cost optimization for an agent that resolves support tickets?

- A. Cost per input token across all requests.
- B. Total monthly tokens consumed by the agent.
- C. Average response length in tokens.
- D. Cost per successfully resolved ticket, including retries and human rework.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** The business pays per outcome. A cheaper configuration that fails more can cost more after retries and escalations.

- **A fails:** Per-token price ignores how many tokens and attempts a resolution takes.
- **B fails:** Volume rises with success. It isn't efficiency.
- **C fails:** Length is a proxy that says nothing about resolution.

*Objective:* Optimize token usage, latency, and cost-performance trade-offs

</details>

### Q39

Which TWO conditions should trigger alerts for a production Claude system? **(Choose TWO.)**

- A. Any single user complaint about tone.
- B. A sustained drop in sampled LLM-judge scores against the baseline.
- C. Any request that uses more than 1,000 tokens.
- D. Refusal rate or schema-failure rate rising above a set threshold.
- E. The model name appearing in application logs.

<details><summary>Answer</summary>

**Answer: B, D**

**Why B, D wins:** Alert on sustained drift in quality and safety signals measured against thresholds.

- **A fails:** A single complaint is noise for paging. Track it as a trend.
- **C fails:** Normal usage. It would page constantly.
- **E fails:** Expected and harmless.

*Objective:* Monitor system performance using logging and observability tools

</details>

### Q40

Input costs doubled week over week with flat traffic. Usage logs show cache_read_input_tokens fell to near zero right after a deploy that added the current timestamp at the start of the system prompt. What is the fix?

- A. Switch to a cheaper model to offset the higher input cost.
- B. Move the workload to the Message Batches API.
- C. Move the timestamp after the static content so the cached prefix is identical across requests.
- D. Raise the organization's rate limits.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Caching matches exact prefixes. A changing value at the top invalidates the cache on every request.

- **A fails:** Treats the symptom and may cost quality.
- **B fails:** Asynchronous. Changes the product, not the cause.
- **D fails:** Unrelated to cost.

*Objective:* Optimize token usage, latency, and cost-performance trade-offs

</details>

---

## D5: Governance, Safety & Risk Management

### Q41

A procurement agent approves purchase orders. Policy says orders over $10,000 need a director's approval. The rule is in the system prompt, yet logs show three violations last month. What is the best fix?

- A. Restate the rule in capital letters at the top and bottom of the system prompt.
- B. Enforce the threshold in the approval tool or a pre-tool check: calls over $10,000 are blocked and routed to a director's queue.
- C. Log every approval over $10,000 for the monthly audit.
- D. Switch to a more capable model that follows instructions more reliably.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** A rule that must always hold is enforced deterministically in code, outside the model.

- **A fails:** Prompt as policy, louder.
- **C fails:** Watch, don't remove. It records violations after they happen.
- **D fails:** Bigger model. Still best effort.

*Objective:* Implement guardrails and safety controls

</details>

### Q42

A public chatbot that can create support tickets screens inputs with a moderation classifier. The classifier times out on 1% of requests. What should happen to those requests?

- A. Process them normally to protect the user experience.
- B. Retry the classifier until it responds, however long that takes.
- C. Ask the main model, in the same call, whether the input is safe and proceed if it says yes.
- D. Fail closed: respond without tool access, offer a retry or a human, and log the event.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** When a control fails, the system should fail closed for consequential capabilities and degrade gracefully for the user.

- **A fails:** Fails open. Unscreened input reaches tools.
- **B fails:** Unbounded latency. Users abandon.
- **C fails:** The screened input is grading itself, which defeats the control.

*Objective:* Implement guardrails and safety controls

</details>

### Q43

An agent reads inbound customer emails and has tools to search the CRM and send emails. What is the biggest risk class, and what is the primary mitigation?

- A. Indirect prompt injection through email content. Limit capabilities (no arbitrary recipients, no bulk exports), require approval for messages to new recipients, and treat email text as data.
- B. Hallucination. Set temperature to 0 for every call.
- C. Latency. Stream responses to users.
- D. Bias. Remove sender names before processing.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Untrusted content plus tools that can send data out is the classic injection-to-exfiltration path. Capability limits hold even when detection misses.

- **B fails:** Real but secondary, and temperature 0 doesn't prevent it.
- **C fails:** Not a safety risk.
- **D fails:** Not the dominant risk for this design.

*Objective:* Identify risks, limitations, and failure modes of LLM systems

</details>

### Q44

A clinical-information assistant refuses 12% of legitimate clinician questions about drug dosing. What should the architect do first?

- A. Remove all safety guidance from the system prompt.
- B. Move to a different model provider.
- C. Build an eval set of legitimate clinician queries, measure the false-refusal rate, adjust the context (verified clinician audience, scope) and classifier thresholds, and re-measure harmful-output rate.
- D. Tell clinicians to rephrase questions that get refused.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Over-refusal is a failure mode to measure and tune against, while watching the safety metric on the other side.

- **A fails:** Over-correction. It trades one failure for another.
- **B fails:** Unmeasured switch.
- **D fails:** Shifts the burden to users and hides the problem.

*Objective:* Identify risks, limitations, and failure modes of LLM systems

</details>

### Q45

Which human-in-the-loop routing is best for an insurance claims assistant?

- A. An adjuster reviews every claim before any action, regardless of value or confidence.
- B. Auto-approve low-value claims with high calibrated confidence. Route low-confidence, high-value, or irreversible decisions (denials) to adjusters. Sample auto-approvals for QA.
- C. Route by the confidence score Claude reports for each claim.
- D. Process all claims automatically and review those that later get complaints.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Route review effort by confidence, reversibility, and cost of a wrong answer, using calibrated thresholds.

- **A fails:** Over-engineering. Reviewer fatigue leads to rubber-stamping.
- **C fails:** Self-reported confidence is not calibrated.
- **D fails:** Watch, don't remove. Errors reach customers first.

*Objective:* Apply human-in-the-loop validation strategies

</details>

### Q46

A US hospital wants Claude to summarize patient records containing PHI. What must be in place before any PHI is sent?

- A. A system-prompt instruction telling Claude not to store or repeat PHI.
- B. Client-side encryption of prompts, with keys held by the hospital.
- C. Removal of patient names, with all other record content sent as-is.
- D. A Business Associate Agreement covering the service and the specific features in use, plus minimum-necessary data and access controls.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** HIPAA requires a BAA with any vendor handling PHI, and coverage depends on the features used.

- **A fails:** Prompt as policy. Not a legal or technical control.
- **B fails:** The model can't process ciphertext.
- **C fails:** Names are one of many identifiers. The rest is still PHI.

*Objective:* Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP)

</details>

### Q47

An EU retailer's support assistant processes customer personal data. Which TWO controls address GDPR obligations? **(Choose TWO.)**

- A. Redact personal data the task does not need before it reaches the model (data minimization).
- B. Rely on the model's privacy training to avoid retaining personal data.
- C. Process data in-region or under a valid transfer mechanism, with a data processing agreement with the vendor.
- D. Add a privacy notice to the system prompt.
- E. Keep full conversation logs indefinitely for audit purposes.

<details><summary>Answer</summary>

**Answer: A, C**

**Why A, C wins:** Minimization and lawful processing location with a DPA are architectural controls that map to GDPR obligations.

- **B fails:** Model behavior is not a compliance control.
- **D fails:** The model reading a notice doesn't inform users or limit processing.
- **E fails:** Violates storage limitation.

*Objective:* Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP)

</details>

### Q48

A resume-screening assistant removed name and gender fields, and the team says it is now fair. What is the best next step?

- A. Ship it. Protected attributes are no longer visible to the model.
- B. Add 'evaluate all candidates without bias' to the system prompt.
- C. Evaluate outcomes on a test set with demographic variation and monitor selection rates by group, since proxies remain. Keep humans making the decision and disclose AI use.
- D. Use a larger model, which shows less bias.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Proxies such as schools, locations, and gaps carry protected information. Fairness is shown by measuring outcomes, not by deleting columns.

- **A fails:** Fairness by deletion is unproven.
- **B fails:** Prompt as policy.
- **D fails:** Bigger model. No measurement.

*Objective:* Address ethical AI considerations (bias, fairness, transparency)

</details>

---

## D6: Stakeholder Communication & Lifecycle Management

### Q49

A COO opens the first meeting with 'we want AI for operations.' What is the best opening move for the architect?

- A. Ask about current processes, volumes, the metrics the COO reports, the cost of errors, and constraints such as data, compliance, and budget.
- B. Demo the newest model's capabilities to show what is possible.
- C. Propose a multi-agent reference architecture to anchor the conversation.
- D. Ask which vector database and cloud provider the company prefers.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Discovery starts from the business problem and its measures, so the design traces back to the business case.

- **B fails:** Solution-first. Requirements are still unknown.
- **C fails:** Architecture before requirements.
- **D fails:** Technology questions before the problem is understood.

*Objective:* Conduct structured discovery and requirement gathering

</details>

### Q50

The CFO must choose between two model configurations for a claims summarizer. How should the architect present the choice?

- A. Show public benchmark leaderboard scores for both models.
- B. Explain the architectural differences between the two models.
- C. For each option: cost per claim and per month, accuracy on the company's eval set and the risk of errors, latency against the SLA, and what reversing the decision would take, plus a recommendation.
- D. Recommend the most capable model, since quality always matters most in claims.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Executives act on cost, risk, and reversibility in their own terms, with a clear recommendation.

- **A fails:** Generic benchmarks don't reflect this workload.
- **B fails:** Not decision-relevant for a CFO.
- **D fails:** Over-engineering, and no trade-off is shown.

*Objective:* Communicate architectural decisions and trade-offs

</details>

### Q51

Which SLA is most appropriate to agree with stakeholders for an AI drafting tool?

- A. AI responses will always be correct and complete.
- B. p95 latency of 5 s or less; at least 92% of drafts accepted with minor edits in monthly sampled review; fallback to a human queue when degraded; a breach triggers review within two business days.
- C. Accuracy will improve every month after launch.
- D. No SLA, because LLM outputs are nondeterministic.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** SLAs for probabilistic systems use measured thresholds with a defined breach response and fallback.

- **A fails:** Promises determinism the system can't deliver.
- **C fails:** Not measurable or enforceable.
- **D fails:** Abdicates expectation alignment.

*Objective:* Manage stakeholder feedback loops and expectation alignment (including SLAs)

</details>

### Q52

Two months after launch, accuracy on a newly added product line is 15 points below the others. Other categories are stable. What should the team do?

- A. Re-architect to a multi-agent design with one agent per product line.
- B. Switch to a different model vendor.
- C. Pause the whole system until the issue is resolved.
- D. Iterate locally: add the new line's documents and examples to retrieval and the eval set, tune, and verify. Re-architect only if the structure can't support it.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** A local failure calls for local iteration with evals. Re-architecture is for structural failures.

- **A fails:** Over-engineering for a content gap.
- **B fails:** Unmeasured and unrelated to the gap.
- **C fails:** Over-reaction. Other categories work.

*Objective:* Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

</details>

### Q53

The architect leaves the project in three weeks. Which TWO items must the handoff include so the system survives their absence? **(Choose TWO.)**

- A. Runbooks that map known failure symptoms to first actions and owners.
- B. The architect's personal API keys so services keep running.
- C. A slide deck summarizing the original vision.
- D. The eval suite with thresholds and instructions to run it before any prompt or model change.
- E. A recorded verbal walkthrough instead of written documentation.

<details><summary>Answer</summary>

**Answer: A, D**

**Why A, D wins:** The team must diagnose issues and ship changes safely without the architect. Runbooks and the eval gate make that possible.

- **B fails:** Security failure. Credentials belong to service identities, not people.
- **C fails:** Vision without operational detail.
- **E fails:** Not searchable or maintainable.

*Objective:* Document architectures and provide implementation guidance

</details>

### Q54

Anthropic announces the deprecation of the model snapshot your production system uses. What is the best response?

- A. Wait until the retirement date, then switch to the newest model alias.
- B. Treat it as a review trigger: run the eval suite on the successor snapshot, fix regressions, migrate to a pinned snapshot ID before retirement, and inform stakeholders.
- C. Switch to the successor immediately without testing, since newer models are better.
- D. Take no action. Deprecated models keep working indefinitely.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Deprecations are planned lifecycle events. Evals gate the migration, and pinned snapshots keep behavior stable.

- **A fails:** Last-minute and alias-based, so behavior can change without warning.
- **C fails:** Skips the eval gate.
- **D fails:** Retired models stop serving requests.

*Objective:* Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

</details>

### Q55

An enterprise prospect requires every workload to run inside its AWS account, under its existing AWS commitment, with data-residency controls. Its team asks about the direct Claude API. What do you recommend?

- A. The direct Claude API, because new features usually arrive there first.
- B. Wait until all access routes reach full feature parity before choosing.
- C. Claude through Amazon Bedrock, because the procurement and residency constraints rule out other routes before latency or cost; flag any feature-availability differences.
- D. Let each team pick its own route so they can compare later.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Governance and procurement constraints eliminate options before any other trade-off applies.

- **A fails:** Ignores the hard constraint.
- **B fails:** Stalls the project indefinitely.
- **D fails:** Fragmented governance and duplicated security review.

*Objective:* Communicate architectural decisions and trade-offs

</details>

### Q56

Midway through design, you learn the team assumed every document is in English. About 20% are in Spanish. What is the right practice?

- A. Proceed as planned, since the model handles Spanish.
- B. Quietly add a translation step and mention it at launch.
- C. Drop Spanish documents from scope to stay on schedule.
- D. Record assumptions explicitly in the requirements, validate them with stakeholders, add Spanish cases to the eval set, and design for them.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Undocumented assumptions become unagreed requirements. Make them explicit, validate them, and test them.

- **A fails:** Untested assumption. Quality in Spanish is unmeasured.
- **B fails:** Hides a design change from stakeholders.
- **C fails:** Silently cuts scope the business needs.

*Objective:* Conduct structured discovery and requirement gathering

</details>

---

## D7: Developer Productivity & Operational Enablement

### Q57

Security requires that no developer can run Claude Code in bypass-permissions mode or connect unapproved MCP servers. Where should this be configured?

- A. In each repository's CLAUDE.md file.
- B. In managed (enterprise) settings deployed to every machine.
- C. In each developer's ~/.claude/settings.json.
- D. In the team wiki's onboarding checklist.

<details><summary>Answer</summary>

**Answer: B**

**Why B wins:** Managed settings take precedence and can't be overridden by users or projects.

- **A fails:** Guidance, not enforcement.
- **C fails:** Developers can change their own files.
- **D fails:** Documentation is not enforcement.

*Objective:* Configure Claude tools and environments for teams (e.g., Claude Code)

</details>

### Q58

New hires' Claude Code sessions ignore the repo's testing conventions, while veterans' sessions follow them. Veterans keep the conventions in ~/.claude/CLAUDE.md. What is the fix?

- A. Ask each new hire to copy a veteran's personal CLAUDE.md file.
- B. Move new hires to a more capable model.
- C. Add the conventions to each developer's local settings file.
- D. Move the conventions into the project CLAUDE.md committed to the repository.

<details><summary>Answer</summary>

**Answer: D**

**Why D wins:** Team conventions belong at the shared project scope so every session in the repo gets them.

- **A fails:** Manual and drifts over time.
- **B fails:** Bigger model. It can't follow conventions it never sees.
- **C fails:** Personal scope again.

*Objective:* Configure Claude tools and environments for teams (e.g., Claude Code)

</details>

### Q59

A team wants Claude to review every pull request automatically, with structured output that a bot posts as comments. What is the best setup?

- A. Run Claude Code in headless mode in CI (for example through the GitHub Action) with JSON output and a scoped tool allowlist. Humans still approve merges.
- B. Ask developers to paste each diff into a chat session and copy the review back.
- C. Let the session that wrote the code review and merge its own pull request.
- D. Run an interactive Claude Code session on a shared server that the team takes turns using.

<details><summary>Answer</summary>

**Answer: A**

**Why A wins:** Headless mode is built for CI. Structured output feeds the bot, and human approval keeps review discipline.

- **B fails:** Manual and inconsistent.
- **C fails:** The author shares its own blind spots. Use an independent reviewer.
- **D fails:** Not automated.

*Objective:* Improve developer workflows using AI-assisted tooling

</details>

### Q60

A production agent's answers degrade overnight, and on-call engineers page the architect every time. What is the best long-term fix?

- A. Keep the architect on the on-call rotation permanently.
- B. Move the agent to a more capable model.
- C. Build runbooks that map symptoms to architectural causes (retrieval, prompt version, model change, tool errors), with traces, dashboards, and an eval command the team can run.
- D. Disable the agent automatically whenever quality drops.

<details><summary>Answer</summary>

**Answer: C**

**Why C wins:** Connecting symptoms to causes and giving the team tools builds self-sufficiency.

- **A fails:** The system stays dependent on one person.
- **B fails:** Bigger model without a diagnosis.
- **D fails:** Over-reaction, and it builds no capability.

*Objective:* Support debugging and operational issue resolution

</details>
