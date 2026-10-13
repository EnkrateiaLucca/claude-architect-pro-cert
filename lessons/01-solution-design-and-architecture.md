# Lesson 1: Solution Design & Architecture

**Exam domain:** D1 (17%, ~11 items) · **Time in session:** Segment 1, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Translate business problems into Claude-based AI solutions
- Design end-to-end architectures (input → processing → output → feedback loops)
- Select appropriate architectural patterns (workflow, agentic, augmented LLM)
- Design multi-agent systems and orchestration strategies
- Apply decomposition techniques for complex problem solving
- Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)

The official prep course says four decisions come before you build, **in this order**. Getting them out of order is "the most reliable path to an expensive pivot."

1. **Ownership:** what work does Claude own, what stays with existing systems, and what stays with a human?
2. **Shape:** augment a live interaction, automate a workflow, or deploy an agent?
3. **Reference architecture:** which named pattern are you committing to?
4. **Entry point:** where does the work meet Claude (model, context strategy, surface)? Lessons 2 and 3 cover this.

## Key ideas

### Decision 1: split the work three ways

Use the four properties of generative AI from Anthropic's *AI Capabilities and Limitations* course as the lens. Each property tells you what Claude should **not** own.

| Property | Limitation | So this belongs to... |
|---|---|---|
| **Next-token prediction** | Fabrication concentrates in specifics: numbers, IDs, citations | **Systems** own calculations, lookups, and exact figures |
| **Knowledge** | Stale after the training cutoff, uneven on niche or private data | **Retrieval or live tools** own facts that change |
| **Working memory** | Attention is finite; buried details get missed | **Systems** own state, records, and long histories |
| **Steerability** | Long chains drift; instructions are best effort | **Code** owns control flow and hard rules |

Claude owns language-shaped judgment: reading, classifying, summarizing, drafting, reasoning over supplied context. **Humans** own accountability for consequential, irreversible, or regulated decisions.

### Decision 2: the shape of the work

| Shape | Looks like | Latency budget | Default pattern |
|---|---|---|---|
| **Augment** | Copilot inside a live call or editor; human accepts or edits | Seconds | Single augmented-LLM call, streaming |
| **Automate** | Back-office pipeline with known steps | Minutes to hours | Workflow (often batch) |
| **Agent** | Open-ended goal; steps unknown in advance; acts on tools | Minutes | Agent loop with guardrails |

### Decision 3: pick the simplest pattern that works

Anthropic's *Building effective agents* defines the ladder. Climb a rung only when evals show the simpler rung fails.

| Rung | Definition | What it costs you |
|---|---|---|
| **Augmented LLM** | One call with retrieval, tools, and memory | Least flexible |
| **Workflow** | LLM calls orchestrated through **predefined code paths** | Can't adapt to surprises |
| **Agent** | LLM **dynamically directs** its own process and tool use in a loop | Latency, tokens, compounding errors, harder to test |
| **Multi-agent** | Orchestrator delegates to subagents with separate context windows | About **15× the tokens** of a chat in Anthropic's research system |

The five workflow patterns and their exam cues:

| Pattern | Use when | Example |
|---|---|---|
| **Prompt chaining** | The task splits into fixed sequential steps; add programmatic **gates** between them | Outline → check outline → write |
| **Routing** | Inputs fall into distinct categories that need different handling | Easy questions to a small model, hard ones to a large one |
| **Parallelization** | *Sectioning:* independent subtasks run at once. *Voting:* same task several times for confidence | Guardrail screen in parallel with the answer; 3 reviewers vote on a vulnerability |
| **Orchestrator-workers** | Subtasks can't be predicted until the input is seen | Multi-file code change, multi-source search |
| **Evaluator-optimizer** | Clear criteria exist and iteration measurably improves output | Translation refinement, policy-compliant drafting |

**Agent vs. workflow:** if you can draw the flowchart in advance, it is a workflow. Agents fit when the number of steps is unpredictable and the environment gives ground truth at each step (tool results, test runs). Give every agent a stopping condition (max turns, budget) and a sandbox.

### Multi-agent systems

From Anthropic's multi-agent research system write-up:

- Multi-agent beat a single agent by **90.2%** on Anthropic's internal research eval. Token usage alone explained most of the performance variance.
- Agents use about **4×** the tokens of chat. Multi-agent systems use about **15×**. The task value must pay for that.
- **Good fit:** breadth-first, parallelizable work whose information exceeds one context window (research, many independent sources).
- **Poor fit:** tightly coupled work where every agent needs the same context, such as most coding.

Orchestration rules the exam rewards:

- **Subagents do not inherit the orchestrator's context.** Pass the task, constraints, and output format explicitly.
- Give each subagent a **clear boundary** so two agents don't duplicate work.
- **Scope tools per subagent.** A summarizer needs no write tools.
- The orchestrator **synthesizes** and checks coverage. It does not just concatenate.
- Scale effort to the query: one agent for a fact lookup, many for a broad survey.

### Decomposition techniques

| Technique | Split by | Use when |
|---|---|---|
| **Pipeline** | Stage (extract → validate → transform → write) | Steps are known and each output can be checked |
| **Map-reduce** | Data partition (per document, per file), then combine | Volume exceeds one context; items are independent |
| **Local + integration pass** | Per-file analysis, then one cross-file pass | Large reviews where one giant prompt dilutes attention |
| **Specialist** | Capability (retrieval agent, analysis agent, writer) | Different tools or prompts per step |
| **Plan-then-execute** | A planning call produces steps; execution follows | Goal is clear but the path depends on the input |

### Reference architectures

| Problem shape | Reference architecture |
|---|---|
| Q&A over a large, slow-changing document set | **RAG**: chunk → embed + BM25 → rerank → generate with citations |
| Questions about **live state** (order status, balance, inventory) | **Tool call to the system of record.** Retrieval over a stale index is the wrong owner for live data |
| High-volume extraction from documents | **Batch pipeline** with structured outputs and schema validation |
| Customer-facing support with actions | **Tool-using agent** with least-privilege tools and human approval for irreversible actions |
| Code changes across a repo | **Coding agent** (Claude Code / Agent SDK) |
| Broad research across many sources | **Orchestrator-workers** multi-agent |

### End-to-end: close the loop

Every design names four stages: **input** (sources, validation, screening) → **processing** (pattern, model, context) → **output** (format, validation, delivery) → **feedback loop** (user corrections, escalations, and eval failures flow back into the eval set and the next prompt version). A design with no feedback loop cannot improve and cannot detect drift.

### Business value pillars

Name the pillar and its metric before you design.

| Pillar | Metric example |
|---|---|
| **Efficiency** | Handle time per ticket, documents processed per hour |
| **Productivity** | Output per employee, cycle time |
| **Transformation** | New capability (24/7 multilingual support) |
| **Cost** | Cost per task vs. the human baseline |
| **Performance SLAs** | p95 latency, availability, accuracy floor |

## Exam traps

- **Agent by default.** If the steps are known, an agent adds cost and risk. Choose a workflow.
- **Multi-agent for coupled work.** Shared-context tasks lose more to coordination than they gain from parallelism.
- **Assuming subagents share memory.** They start with only what you pass them.
- **RAG for live data.** An index refreshed nightly cannot answer "where is my order right now."
- **No feedback loop.** An architecture without one fails the "end-to-end" objective.

## Exercise

`exercises/01-pattern-selection.md`: five business problems. For each, split ownership, name the shape, pick the pattern, and say what it costs.

## Check yourself

1. Monthly invoice extraction: same five steps every time, 40,000 invoices. Pattern?
2. A team proposes four subagents for a refactor where every change depends on shared types. Your concern?
3. A support bot answers "where is my package?" from a nightly index. What is wrong?

<details>
<summary>Answers</summary>

1. A workflow (prompt chain with validation gates) run through the Message Batches API. Known steps and no urgency rule out an agent.
2. The work is tightly coupled. Subagents with separate contexts will conflict. Use a single agent, or decompose by independent modules first.
3. Retrieval is doing a job that live state should own. Call the shipping system's API as a tool.

</details>

## Official resources

- Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- AI Capabilities and Limitations (four properties): https://academy.claude.com/courses/ai-capabilities-and-limitations
- Official prep course 1, Claude Platform & Solution Design: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
