# Exercise 6: Discovery and a One-Page ADR

**Lesson:** 06 · **Time:** 15 minutes · **Format:** role-play with Claude, then write

## Part 1: Discovery (role-play)

Paste this into Claude (any model) and run the discovery yourself:

```
You are Dana, VP of Customer Operations at a mid-size e-commerce company. You are not technical.
You asked an architect for "an AI that handles customer emails." Answer my questions in character.
Facts you know (reveal only when asked directly): 18,000 emails/week, 60% are "where is my order",
15% returns, 10% billing disputes, the rest mixed. Team of 22 agents, average handle time 6 minutes.
You report CSAT and cost per contact to the CFO. Billing disputes have caused two regulator complaints
this year. Orders live in Shopify, tickets in Zendesk. Legal says customer data must stay in the EU.
Budget: you'd be happy with 30% lower cost per contact within two quarters.
After I say "DONE", score my discovery out of 10: did I find volume, baseline, success metric,
cost of errors, data location, constraints, and budget? List what I missed.
```

Aim to uncover everything in under 10 questions. Do not mention models, vector databases, or frameworks.

## Part 2: One-page ADR

Using what you learned, write an ADR for the core decision: **how should "where is my order" emails be handled?**

Template:

```
# ADR-001: <decision>
Context:        <business problem, constraints, success metric>
Options:
  1. <option>   Cost: …  Risk: …  Reversal: …
  2. <option>   Cost: …  Risk: …  Reversal: …
  3. <option>   Cost: …  Risk: …  Reversal: …
Decision:       <chosen option and why>
Consequences:   <what we accept>
Reopen if:      <trigger that would change the decision>
```

<details><summary>Reference ADR</summary>

```
# ADR-001: Automate "where is my order" (WISMO) replies with a live order lookup

Context: 18k emails/week; ~60% WISMO. Goal: −30% cost per contact in two quarters
without CSAT loss. Orders in Shopify, tickets in Zendesk. Customer data must stay in the EU.

Options:
  1. RAG over a nightly export of orders
     Cost: low build. Risk: answers stale order status (wrong for live data). Reversal: easy.
  2. Workflow: classify intent → call the Shopify order API (tool) → draft reply → auto-send
     if the order is found and the classification is confident, otherwise route to an agent
     Cost: ~2 weeks build, low per-email cost (small model + caching).
     Risk: misclassification sends the wrong template; mitigated by confidence threshold
     and weekly sampling. Reversal: turn off auto-send (config flag).
  3. Autonomous agent with full Shopify + Zendesk access
     Cost: higher tokens and testing. Risk: excessive agency (refunds, edits) for a read-only
     need. Reversal: moderate.

Decision: Option 2. WISMO is a known-step task with live data, so a workflow with a
live tool fits; an agent adds cost and risk without benefit.

Consequences: Billing disputes stay with humans (regulator exposure). EU-region deployment
route required. Eval gate: ≥ 97% correct status on 500 labeled emails before auto-send.

Reopen if: CSAT for automated replies drops > 2 points, the confident share falls below
70%, or a new channel (chat) needs the same capability.
```

</details>
