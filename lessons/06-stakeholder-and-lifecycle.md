# Lesson 6: Stakeholder Communication & Lifecycle Management

**Exam domain:** D6 (14%, ~9 items) · **Time in session:** Segment 4, about 12 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Conduct structured discovery and requirement gathering
- Communicate architectural decisions and trade-offs
- Manage stakeholder feedback loops and expectation alignment (including SLAs)
- Document architectures and provide implementation guidance
- Support lifecycle phases (discovery, design, handoff, monitoring, iteration)

The official prep course frames D6 as three meetings: **discovery** (where the real requirements are set), **approval** (where a trade-off is won or lost), and **handoff** (where the design survives your absence or quietly degrades).

## Key ideas

### Discovery: requirements before architecture

A design must trace back to the business case, not to the architect's technical preference. Structured discovery captures:

| Ask about | Why it shapes the architecture |
|---|---|
| The decision or task, and who does it today | Sets the **baseline** you must beat and the human role that remains |
| Volume and peaks | Drives cost model, rate limits, batch vs. real time |
| Latency the user will tolerate | Live call (seconds) vs. back office (hours) decides sync vs. async and model tier |
| Cost of a wrong answer, and whether it can be undone | Decides review routing and guardrails (Lesson 5) |
| Data: where it lives, how sensitive, how fresh | Decides RAG vs. live tool lookup, residency, and redaction |
| Regulatory and procurement constraints | Can rule out entry points before any other trade-off (e.g., must run in the customer's cloud) |
| What "success" means, in a number | Becomes the eval suite and the SLA |

Write down every **assumption** you make. An undocumented assumption becomes a requirement nobody agreed to.

**Non-technical stakeholders** describe outcomes ("faster claims"), not systems. Ask for the current process, a recent example, and the metric they report upward. Do not open with model or framework choices.

### Present trade-offs a stakeholder can act on

Each option in a decision review pairs three things:

| Element | Example |
|---|---|
| **Cost** | "$0.04 per ticket, about $9k per month at current volume" |
| **Risk** | "Opus answers 3 points more accurately on our eval, but p95 latency rises from 4 s to 11 s" |
| **Reversal** | "Switching back is a config change" vs. "re-indexing 2M documents" |

Business terms beat technical terms. "Prompt caching" means nothing to a CFO. "Cuts input cost on repeated context by up to 90%" does. Present a **recommendation**, the credible alternatives, and what would make you change your mind. A review that ends without a decision usually lacked the reversal cost.

Record each decision in an **Architecture Decision Record (ADR)**: context, options considered, decision, consequences, and the trigger that would reopen it.

### Feedback loops and SLAs

LLM systems are probabilistic. Set expectations in measured terms: "92% on the golden set, reviewed weekly." Never promise "always correct."

| Loop element | What to define up front |
|---|---|
| **SLA / SLO** | Latency (p50/p95), availability, quality floor on the eval suite, cost ceiling |
| **Review triggers** | Eval score drop, SLA breach, user complaint spike, model deprecation notice, new regulation |
| **Breach response** | Who is paged, the fallback (smaller model, cached answer, human queue), the deadline for a fix |
| **Iterate vs. re-architect** | Iterate when the failure is local (a prompt, a retrieval setting). Re-architect when the failure is structural (wrong pattern, data no longer fits the store, volume outgrew the design) |
| **Governance checkpoints** | Built into the same loop: compliance review at each major change |

### Documentation and handoff

A design that only the architect understands is a liability. The handoff package:

- Architecture diagram and data-flow diagram (where data goes, what is logged, what is retained)
- ADRs for the major decisions
- Prompt and config registry with versions
- The eval suite, its thresholds, and how to run it
- Runbooks: known failure modes → symptom → first action → owner
- Named owners for each component, control, and compliance obligation

The test of a good handoff: the team can ship a prompt change, run the evals, and roll back without calling the architect.

### Lifecycle phases

| Phase | Architect's job | Exit evidence |
|---|---|---|
| **Discovery** | Requirements, assumptions, success metric, constraints | Signed-off requirements + baseline |
| **Design** | Pattern, model, context strategy, controls, entry point | ADRs + eval plan |
| **Build / POC** | Prove feasibility on real data | Eval results vs. success criteria |
| **Handoff** | Docs, runbooks, owners, training | Team runs a change end to end |
| **Monitoring** | Dashboards, alerts, review cadence | SLO reports |
| **Iteration** | Evals gate every change (prompt, model, retrieval) | Before/after eval comparison |

**Model lifecycle.** Models move Active → Legacy → Deprecated → Retired, and requests to a retired model fail. Anthropic gives at least **60 days' notice** before retiring a publicly released model; Bedrock and Google Cloud set their own dates. Pin a specific model ID in configuration (current dateless IDs are pinned snapshots; older dated models also had floating aliases). Treat a deprecation notice as a review trigger: run the eval suite on the successor, re-baseline cost and latency, fix regressions, then migrate.

**Pilot to production.** Anthropic's enterprise guidance: pick a first use case that is business-critical but low security risk, with a measurable metric; resist starting with the biggest opportunity; and agree **graduation criteria** up front (performance thresholds, operational readiness, risk infrastructure) so the pilot doesn't stall in limbo.

### Entry point and go-to-market

The official prep course has the architect compare the **direct Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry** routes on latency, compliance, and cost. Procurement and compliance often decide first: an enterprise with an AWS commit, data-residency rules, or FedRAMP needs will route through its cloud provider. In a partner sales motion, the architect leads discovery, a scenario-based demo on the customer's real problem, technical objection handling, and joint scoping. The output is an **outcome document** that states value in the sponsor's metric.

## Exam traps

- **Leading discovery with technology.** "Which vector database do you prefer?" is the wrong first question. Ask about the process, the metric, and the cost of errors.
- **Promising determinism.** An SLA of "100% accurate" is a wrong answer. Measured thresholds with a breach response are right.
- **Re-architecting on a local failure.** One bad prompt does not justify a new pattern. Fix locally, re-run evals.
- **Handoff = a slide deck.** Without runbooks, evals, and owners, the design degrades after you leave.
- **Ignoring the procurement constraint.** If the stem says "must stay in the customer's AWS account", the direct API is out before latency or cost matter.

## Exercise

`exercises/06-discovery-and-adr.md`: run a discovery on a vague request, then write a one-page ADR with cost, risk, and reversal for each option.

## Check yourself

1. A VP asks for "an AI that handles claims." What do you ask first?
2. Name the three elements to pair with each option in a trade-off presentation.
3. The eval score drops 6 points after the vendor announces a model deprecation and you switch to the successor. Iterate or re-architect?

<details>
<summary>Answers</summary>

1. How claims are handled today, the volume, the metric the VP reports, and the cost of a wrong decision. Not the model or the stack.
2. Cost, risk, and what a reversal would take.
3. Iterate first. The failure follows a model change, so tune prompts against the eval suite on the successor. Re-architect only if the structure no longer fits.

</details>

## Official resources

- Define success criteria: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Deploying AI from pilot to production: https://claude.com/blog/deploying-ai-from-pilot-to-production
- Model deprecations: https://platform.claude.com/docs/en/about-claude/model-deprecations
- Models overview: https://platform.claude.com/docs/en/models/overview
- Official prep course 4, Stakeholder Engagement, Lifecycle & GTM: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
