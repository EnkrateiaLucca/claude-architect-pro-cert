# Official Prep Path: Claude Certified Architect – Professional Prep Course

The Anthropic Partner Academy hosts a five-course prep path for CCAR-P at https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional. Registration requires a Partner Academy account. The notes below record only the public structure of each course (title, blurb, table of contents, screen and checkpoint counts). Course content itself is not reproduced here.

Path blurb (abridged): the Architect is involved once the question shifts from "can Claude do the task" to "will the systems around Claude integrate and operate as needed." The path covers what work Claude owns, what form that work takes, which architecture fits, and where each control sits.

## Mapping to the exam blueprint

| Prep course | Minutes | Exam domains it serves |
|---|---|---|
| 1. Claude Platform & Solution Design | 238 | D1 Solution Design & Architecture (17%), D2 Models, Prompting & Context (13%), part of D3 (RAG) |
| 2. Enterprise Integration & Production | 158 | D3 Integration (19%), D4 Evaluation, Testing & Optimization (16%) |
| 3. Responsible AI, Safety & Risk for Architects | 114 | D5 Governance, Safety & Risk (14%) |
| 4. Stakeholder Engagement, Lifecycle & GTM | 178 | D6 Stakeholder Communication & Lifecycle (14%) |
| 5. Team Enablement & Operational Productivity | 45 | D7 Developer Productivity & Operational Enablement (7%) |

The mapping is an inference from section titles. Anthropic does not publish it.

## Course 1 · Claude Platform & Solution Design (238 min)

Framing: four decisions come before building, in this order.

1. What part of the work should Claude own (vs. existing systems vs. a human)?
2. What shape is the work (augment a live interaction, automate a workflow, or deploy an agent that acts on its own)?
3. Which reference architecture are you committing to?
4. Where does the work interact with Claude (entry point, model, context strategy)?

Getting these out of order is described as the most reliable path to an expensive pivot.

Sections (34 screens · 12 sections · 11 checkpoints): Module Introduction · How Claude Behaves · Platform Map & Primitives · Decomposition · Pattern Selection · Reference Architectures · RAG Pipeline Design · Model & Context Strategy · Prompting as Architecture · Entry Points & Governance · Assembly & Recap · Module Complete.

## Course 2 · Enterprise Integration & Production (158 min)

Blurb: the tools that separate a prototype from a production system: evals, cost models, feasibility frameworks, integration architecture, and structured experimentation.

Sections (20 screens · 5 sections · 6 checkpoints): Module Introduction · Evals · POC to Prod · Sizing · Integration · A/B & Obs · Exercise: Eval Framework · Wrap-up.

## Course 3 · Responsible AI, Safety & Risk for Architects (114 min)

Blurb: what controls stop a system from refusing a valid request, producing an unfair outcome, or taking an action no one approved.

Sections (21 screens · 5 sections · 7 checkpoints): Module Introduction · Alignment · Guardrails · Fairness · Review routing · Compliance · Wrap-up · Module Complete.

## Course 4 · Stakeholder Engagement, Lifecycle & GTM (178 min)

Blurb: what happens in the rooms with stakeholders: the discovery conversation where the real requirements are set, the approval meeting where a tradeoff is won or lost, and the handoff where a design either survives the architect's absence or quietly degrades.

Sections (19 screens · 6 sections · 6 checkpoints): Module Introduction · Discovery · Tradeoffs · Feedback Loops · Documentation · Entry Point · Wrap-up · Module Complete.

## Course 5 · Team Enablement & Operational Productivity (45 min)

Blurb: getting people productive with Claude and keeping them productive once the system is live.

Sections (9 screens · 4 sections · 3 checkpoints): Module Introduction · Team Setup · Dev Workflows · Ops Support · Wrap-up · Module Complete.

## Takeaways for this course

- Course 1 is the longest and spans three domains. Weight study time toward design decisions, pattern selection, and RAG.
- Course 2 pairs integration with evals, A/B testing, and observability, which matches D3 + D4 (35% of the exam together).
- Course 3 frames safety as three failure types: over-refusal, unfair outcomes, and unapproved actions. Each needs a named control and a defined failure path.
- Course 4 frames stakeholder work as three meetings: discovery, approval, and handoff.
- Course 5 is short, which matches D7's 7% weight.
