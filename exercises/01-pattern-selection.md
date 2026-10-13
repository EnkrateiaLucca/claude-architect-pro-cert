# Exercise 1: Ownership, Shape, Pattern

**Lesson:** 01 · **Time:** 15 minutes · **Format:** design drill, then compare with the reference

For each problem, fill in four lines:

1. **Ownership:** what Claude does / what existing systems do / what humans do
2. **Shape:** augment, automate, or agent
3. **Pattern:** augmented LLM, a named workflow, agent, or multi-agent
4. **Cost:** what this choice costs you, and what evidence would make you climb or descend a rung

## Problems

**A. Insurance claims intake.** 3,000 claims a day arrive as PDFs and emails. Each needs fields extracted, a policy-coverage check against the policy database, and routing to one of six adjuster queues. Adjusters make the payout decision.

**B. Contact-center copilot.** Agents on live calls want suggested answers from a 1,200-page product manual and the customer's current order status. Answers must appear within 2 seconds.

**C. Competitive research.** A strategy team asks for a weekly brief covering 40 competitors across news, filings, pricing pages, and job posts.

**D. Repo-wide migration.** Migrate a 300-file service from one logging library to another. The changes follow one pattern but every file differs slightly. CI tests exist.

**E. Marketing localization.** Translate campaign copy into 12 languages to a brand style guide. Quality matters more than speed; a native reviewer signs off on each language.

<details><summary>Reference answers</summary>

**A. Claims intake**
- Ownership: Claude extracts fields and classifies the claim type. The policy database (a tool) owns coverage facts. Code owns routing rules. Adjusters own payout decisions.
- Shape: automate.
- Pattern: **prompt-chaining workflow** (extract → validate against schema → coverage lookup tool → route) plus **routing** to queues. Run non-urgent volume through the Message Batches API.
- Cost: no flexibility for odd claims. Send low-confidence or schema-failing claims to a human queue. An agent adds cost without benefit because the steps are known.

**B. Contact-center copilot**
- Ownership: Claude drafts the suggested answer. RAG retrieves manual passages. The order system (a live tool) owns order status. The human agent decides what to say.
- Shape: augment.
- Pattern: **augmented LLM**: one call with retrieval + one order-status tool, streaming, cached system prompt, fast model.
- Cost: limited reasoning depth for a 2-second budget. Climb to a larger model only for question types where evals show the fast one fails, via routing.

**C. Competitive research**
- Ownership: Claude searches, reads, and synthesizes. Code schedules the run and stores the brief. An analyst reviews before distribution.
- Shape: agent (sources and steps vary every week).
- Pattern: **orchestrator-workers multi-agent**: one subagent per competitor group in parallel, the orchestrator synthesizes and checks coverage.
- Cost: about 15× the tokens of a chat. Justified by breadth and parallelism. Pass each subagent its scope and output format explicitly.

**D. Repo-wide migration**
- Ownership: Claude edits files. CI tests own correctness. Engineers review the PRs.
- Shape: agent (coding).
- Pattern: **single coding agent** (Claude Code headless) applied per file or per module (map), with tests as ground truth and a final integration pass. Multi-agent fits poorly if files share types; parallelize only across independent modules.
- Cost: compounding errors over 300 files. Batch the work into reviewable PRs and gate each on CI.

**E. Localization**
- Ownership: Claude translates and self-checks against the style guide. Reviewers own sign-off.
- Shape: automate.
- Pattern: **parallelization (sectioning by language) + evaluator-optimizer** (a second call scores against the style guide and requests revisions).
- Cost: roughly double the calls per language. Worth it because quality outranks speed and the criteria are clear.

</details>
