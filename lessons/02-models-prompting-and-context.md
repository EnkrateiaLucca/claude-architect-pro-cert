# Lesson 2: Claude Models, Prompting & Context Engineering

**Exam domain:** D2 (13%, ~8 items) · **Time in session:** Segment 2, about 15 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Select appropriate Claude models based on trade-offs
- Design system prompts, templates, and guardrails
- Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)
- Optimize context windows and manage token usage
- Implement prompt reuse strategies (caching, modular prompts, Skills)

The objectives name no model versions. The exam tests the **trade-off reasoning**, so learn the reasoning and treat the lineup below as context that will change.

## Key ideas

### Model selection: reason in trade-offs

Current lineup (October 2026, from the models overview and pricing pages):

| Model | Positioning | Input / output per MTok |
|---|---|---|
| **Fable 5.1** | Most demanding reasoning and long-horizon agentic work | $10 / $50 |
| **Opus 5.5** | Long-running agentic coding and knowledge work. Anthropic's "start here if unsure" | $4 / $20 |
| **Sonnet 5.5** | Best combination of speed and intelligence | $2 / $10 |
| **Haiku 5.5** | High-volume, latency-sensitive classification, extraction, routing | $0.10 / $0.50 (≤100k-token prompts) |

All four have a 1M-token context window and 128K max output. Output costs 5× input on every current model.

**The decision rules the exam rewards:**

- **Benchmark on your own eval set.** Anthropic calls use-case tests "the most important step" in a model decision. Public leaderboards don't settle it.
- **Two valid starting strategies.** *Efficiency-first:* start small, upgrade only on a measured capability gap. *Capability-first:* start large, then lower effort or downgrade while evals hold.
- **Effort before model.** "Tuning effort is often a better lever than switching models." Effort (`low` → `max`) changes how much the model thinks and writes.
- **Route by difficulty.** A small model for easy or high-volume steps, a larger one for the hard tail. Verify both on the eval set.
- **Compare cost per completed task**, not price per token.

### System prompts, templates, guardrails

| Element | Put in the system prompt | Keep out of it |
|---|---|---|
| Role and scope | "You assist claims handlers with summaries of medical records" | — |
| Context | Audience, domain background, definitions | Secrets, API keys |
| Behavior guardrails | Stay in scope, cite sources, say "I don't know" | Hard business limits that must always hold (enforce in code) |
| Output contract | Format description | Schema enforcement (use structured outputs) |

**Templates** separate the fixed prompt from variables (`{{customer_tier}}`, `{{document}}`). Version them like code, test them against the eval set, and log the version with every request. Use XML tags to separate instructions, documents, and examples.

API constraints that changed on recent models: **assistant prefill returns an error on Claude 4.6+**, and **forced `tool_choice` returns an error on the newest models**. Use **structured outputs** (JSON schema) or **strict tool use** to guarantee shape.

### Techniques

| Technique | Use when | Note |
|---|---|---|
| **Zero-shot** | Clear, common task | Start here; add only what evals show is missing |
| **Few-shot** | Format, style, or tricky mapping must be exact | 3–5 diverse examples in `<example>` tags, including edge cases |
| **Chain-of-thought** | Multi-step reasoning, analysis, math logic | Current models think adaptively; raise effort, or ask for reasoning in tags before the answer. Send exact arithmetic to a tool |
| **Prompt chaining** | Several distinct subtasks | One focused prompt per step with checks between |

Thinking tokens bill as output tokens. More reasoning costs more; use it where evals show it pays.

### Context windows and token usage

Anthropic's context-engineering goal: "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome." A 1M window does not make more context better. Performance degrades as context fills ("context rot").

| Problem | Technique |
|---|---|
| Long document + question | Document first (in XML tags), question last; ask for relevant quotes before answering |
| Long agent sessions | **Context editing** (clear stale tool results), **compaction** (summarize older turns), **memory tool** (durable facts in files you control) |
| Critical facts get lost | Keep a structured facts block (constraints, IDs, decisions) that survives compaction |
| Knowledge base < ~200k tokens | Put it all in the prompt with caching; skip RAG |
| Budgeting | Count tokens before sending. Newer models' tokenizer produces about 30% more tokens for the same text, so re-baseline cost after a migration |

### Prompt reuse

**Prompt caching** (the exam's favorite optimization):

- Order content **static → dynamic**: tools → system → messages. Caching matches an exact prefix. Any change upstream invalidates everything after it.
- Up to **4** cache breakpoints. Minimum cacheable length is 512 tokens on current models (longer on some older ones); shorter prompts silently don't cache.
- TTL: **5 minutes** (write 1.25× base input) or **1 hour** (write 2×). Reads cost a small fraction of base input (0.1× on most models, less on the newest).
- Cache reads don't count toward input-tokens-per-minute rate limits on most models.
- Anthropic calls caching "the largest lever by a wide margin" for agent-loop cost.
- Silent killers: a timestamp or user ID at the top of the system prompt, reordered tools, changing top-level effort between requests.

**Modular prompts:** shared, versioned components (policy block, tone block, output block) assembled per use case. One fix propagates everywhere.

**Agent Skills:** a folder with `SKILL.md` (name + description in frontmatter), plus optional scripts and references. **Progressive disclosure:** about 100 tokens of metadata per skill sit in context; the body loads when the skill is relevant; bundled files load only when read; script code never enters context, only its output. Skills fit reusable procedures across many tasks. Audit third-party skills like installed software.

## Exam traps

- **Biggest model by default** without an eval. Or the reverse: **smallest model "regardless of task fit."**
- **Hard rules in the system prompt** (refund limits, authorization). Guidance only.
- **Prefill or forced tool choice** to guarantee format on current models. Use structured outputs.
- **Dynamic content before static content** in a cached prompt.
- **"Bigger window" as the fix** for lost-in-the-middle or long sessions. Curate the context instead.

## Exercise

`exercises/02-caching-and-context.md` (design) and `exercises/scripts/prompt_caching.py` (runnable): measure cache writes and reads, then break the cache with one misplaced timestamp.

## Check yourself

1. A 9,000-token policy prompt is identical across requests, but `cache_read_input_tokens` is always 0. The first line of the system prompt is `Today is {date} {time}`. Fix?
2. Which is usually tried first when a capable model's output is a little shallow: switching to a bigger model, or raising effort?
3. Your agent loads 60 internal procedures into every prompt. What mechanism fits better?

<details>
<summary>Answers</summary>

1. Move the date/time after the static content (or drop the time). The changing first line breaks the exact-prefix match.
2. Raising effort. Anthropic calls effort tuning "often a better lever than switching models." Verify on evals.
3. Agent Skills (progressive disclosure), or retrieval if they are reference documents rather than procedures.

</details>

## Official resources

- Models overview: https://platform.claude.com/docs/en/models/overview
- Choosing a model: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- Effort: https://platform.claude.com/docs/en/build-with-claude/effort
- Prompt caching: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Agent Skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Structured outputs: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
