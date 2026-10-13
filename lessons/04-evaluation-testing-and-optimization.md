# Lesson 4: Evaluation, Testing & Optimization

**Exam domain:** D4 (16%, ~10 items) · **Time in session:** Segment 3, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Define evaluation metrics (accuracy, latency, cost, safety, security)
- Design evaluation datasets and test frameworks using mixed methodologies
- Conduct A/B testing and iterative improvements
- Diagnose system issues (prompt failure, hallucinations, model mismatch)
- Optimize token usage, latency, and cost-performance trade-offs
- Monitor system performance using logging and observability tools

The official prep course's rule: **build evals as acceptance criteria before the first line of production code, and use them as the gate before any model or architecture change.**

## Key ideas

### Metrics across five dimensions

| Dimension | Example metrics |
|---|---|
| **Accuracy** | Exact match, F1, rubric score, groundedness/citation accuracy, task success rate |
| **Latency** | Time to first token (TTFT), total latency, p50/p95/p99 |
| **Cost** | Cost per task (not per token), cost per resolved ticket |
| **Safety** | Harmful-output rate, **false-refusal rate**, policy violation rate |
| **Security** | Prompt-injection success rate, data-leak rate, unauthorized tool-call attempts |

Anthropic's success criteria guidance: criteria must be **specific, measurable, achievable, and relevant**. "Good performance" is not a criterion. "F1 ≥ 0.85 on the held-out set, p95 < 3 s, < 0.1% unsafe outputs" is.

### Datasets and mixed methods

**Dataset:** representative real traffic + edge cases + adversarial cases (injections, off-topic, ambiguous) + regression cases from past failures. Keep a held-out set you never tune against.

| Grading method | Strength | Weakness | Use for |
|---|---|---|---|
| **Code-based** | Fast, cheap, deterministic | Only works for checkable outputs | Exact match, classification labels, JSON schema, regex, unit tests |
| **LLM-as-judge** | Scales to nuanced criteria | Probabilistic; must be validated against humans | Tone, helpfulness, faithfulness to sources, rubric scoring |
| **Human** | Gold standard, catches the unexpected | Slow, expensive. Anthropic: "avoid if possible" at scale | Calibrating the judge, high-stakes spot checks |

Anthropic's guidance: **prefer more test cases with automated grading over a few hand-graded ones.** For LLM judges: give a detailed rubric, ask for a discrete score or label, have it reason before scoring, and check its agreement with human labels before trusting it. Use a different prompt (ideally a different model) from the system under test.

**Agent evals.** Start with 20–50 tasks drawn from real failures and read the transcripts. *pass@k* = at least one success in k tries; *pass^k* = all k tries succeed (75% per trial over 3 trials ≈ 42%). Customer-facing agents need pass^k thinking: users see every run.

**Eval stages:** offline evals during development → regression suite in CI on every prompt/model change → online monitoring (sampled LLM-judge scoring of production traffic plus user signals).

### A/B testing and iteration

1. **Hypothesis:** "Adding reranking raises answer accuracy by ≥ 3 points without raising p95 above 4 s."
2. **One variable** changes. Everything else is held constant.
3. **Primary metric + guardrail metrics** (cost, latency, safety must not regress).
4. **Sample size** estimated up front. Small samples on noisy LLM outputs produce false wins.
5. **Read without overclaiming:** report the effect size and uncertainty. A 1-point lift on 50 samples is noise.

Run offline evals first. Run online A/B only on changes that pass offline.

### Diagnose before you change anything

| Symptom | Likely cause | First check |
|---|---|---|
| Wrong answers right after a **document refresh**; model unchanged | Retrieval/indexing (stale or broken index, embedding mismatch) | Inspect retrieved chunks for failing queries |
| Confident fabricated specifics; retrieval looks fine | Hallucination: model answering beyond its context | Require quotes/citations, allow "I don't know", add grounding checks |
| Output ignores format or a rule on some inputs | Prompt failure: ambiguous instruction, conflicting rules, missing examples | Read failing cases; add examples or structured outputs |
| Quality drop after switching to a smaller model | **Model mismatch**: task exceeds model capability | Compare on the eval set; route hard cases to a larger model |
| Quality drop after an upgrade to a newer model | Prompts tuned to old model behavior | Re-run evals; adjust prompts to the new model |
| Works in testing, fails on real traffic | Eval set unrepresentative | Sample production failures into the eval set |

**Diagnose from what changed.** The trigger in the stem points at the layer.

### Optimize tokens, latency, and cost

| Lever | Saves | Note |
|---|---|---|
| **Prompt caching** | Input cost and TTFT on repeated prefixes | Static content first; cache reads cost a fraction of base input |
| **Message Batches API** | 50% cost | Asynchronous, results within 24 h. For non-urgent volume |
| **Model routing** | Cost and latency | Small model for easy/classification steps, larger for hard ones |
| **Effort / thinking budget** | Cost and latency | Lower for routine tasks, higher where evals prove it helps |
| **Output length** | Cost and latency (output tokens cost more than input) | Tight `max_tokens`, concise formats, structured outputs |
| **Context trimming** | Cost, attention | Retrieve fewer, better chunks; compaction for long sessions |
| **Streaming** | Perceived latency | Doesn't reduce total time or cost |
| **Parallel calls** | Wall-clock time | For independent subtasks |

Measure **cost per successful task**. A cheaper configuration that fails more often can cost more after retries and human rework.

### Monitor in production

Log per request: request ID, model and version, prompt version, input/output token counts (including cache reads/writes), latency, `stop_reason`, tool calls and results, retrieval hits, and eval or user-feedback scores. Redact PII before logging. Use distributed tracing (OpenTelemetry) across agent steps. Alert on SLO breaches, cost anomalies, rising refusal rates, and eval-score drift.

## Exam traps

- **Shipping a model swap without evals.** Evals are the gate. No eval, no change.
- **Wrong trigger.** Temperature, weights, and window size are distractors when the stem says "after a document refresh."
- **Optimizing per token instead of per task.**
- **Declaring an A/B winner on a tiny sample.**
- **LLM judge never validated against humans.**
- **Batch API for user-facing latency.** It is asynchronous.

## Exercise

`exercises/04-eval-plan.md` (design) and `exercises/scripts/eval_harness.py` (runnable): build a mixed-method eval with code-based and LLM-judge graders.

## Check yourself

1. Nightly report generation for 20,000 accounts. Fastest cost win with no quality change?
2. An LLM judge rates the new prompt 8% better. What must be true before you trust that?
3. A team switches to a smaller model and accuracy falls on legal-clause questions only. Name the issue and the fix.

<details>
<summary>Answers</summary>

1. The Message Batches API (50% off), plus prompt caching on the shared instructions.
2. The judge was validated against human labels, the test set is representative and large enough, and only the prompt changed.
3. Model mismatch on hard cases. Route legal-clause questions to the larger model and keep the small model for the rest.

</details>

## Official resources

- Define success criteria and build evaluations: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Reduce hallucinations: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Message Batches: https://platform.claude.com/docs/en/build-with-claude/batch-processing
- Official prep course 2, Enterprise Integration & Production: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
