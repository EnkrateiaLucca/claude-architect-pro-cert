# Community Resources for the Claude Certified Architect Exams

## Context

The most-starred community repo for the Claude Certified Architect exams is `paullarionov/claude-certified-architect`. This file records which exam it targets, which official exam guide it mirrors, the testable facts it teaches, how its practice questions work, and where it disagrees with current Anthropic docs. It also briefly reviews other community repos, focusing on any that cover the **Professional (CCAR-P)** exam this course prepares for. Research date: 2026-10-13.

### Source key

| Alias | What it is | URL |
|---|---|---|
| `REPO` | paullarionov repo, shallow clone at commit `11e53a7` (2026-10-02). Paths like `guide_en.md §3.1` refer to this repo. | https://github.com/paullarionov/claude-certified-architect |
| `OG-F-v0.1` | Official Foundations exam guide, "Version 0.1", file dated 2026-03-12 (launch guide) | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773274827%2FClaude+Certified+Architect+%E2%80%93+Foundations+Certification+Exam+Guide.pdf |
| `OG-F-v1.0` | Official Foundations exam guide, v1.0, effective July 2026 | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf |
| `OG-P-v1.0` | Official Professional exam guide, v1.0, effective July 2026 | https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542810/Claude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf |

All three PDFs were downloaded and text-extracted. They are hosted on the Skilljar content CDN that Anthropic Academy uses.

## Findings

### 1. Repo at a glance

- The repo has 5,030 stars and 1,200 forks; it was created 2026-03-14 and last pushed 2026-10-02. [source: https://api.github.com/repos/paullarionov/claude-certified-architect]
- It contains one study guide in 15 languages (`guide_<lang>.md`, ~3,426 lines in English), auto-built PDF and EPUB versions, an HTML practice test in 8 languages, and Anki decks in 8 languages. [source: REPO README.md, file tree]
- The English guide has two parts: Part I "Theory Foundations" (13 chapters organized by technology) and Part II "Exam Domain Notes" (one section per official task statement), followed by 12 example questions, a 76-question practice test, 4 practical exercises, a technology appendix, and an out-of-scope list. [source: guide_en.md headings]
- The README links a NotebookLM "video materials" notebook and a Spanish companion repo that covers Foundations and Professional. [source: REPO README.md "Video Materials", "See Also"]

### 2. Which exam it targets

- The repo targets **Claude Certified Architect – Foundations (CCAR-F)** only. The README title, guide title, and repo description all say "Foundations". [source: REPO README.md; guide_en.md title]
- It does not cover the Professional exam. No CCAR-P domains (RAG, evaluation, governance, stakeholder communication) appear in the guide. [source: guide_en.md full outline]

### 3. Which official exam guide version it mirrors

- The repo mirrors the **March 2026 launch guide (`OG-F-v0.1`)**. Its exam-format table says "Multiple choice (1 correct out of 4)" and "Guessing penalty: None". [source: guide_en.md "Exam Format"]
- `OG-F-v0.1` says the same thing: "Each question has one correct response and three incorrect responses (distractors)" and "there is no penalty for guessing". [source: OG-F-v0.1 "Response Types"]
- `OG-F-v1.0` (July 2026) changed the item format to "Multiple-choice and multiple-response items; each item states how many responses to select". The repo has not picked up this change. [source: OG-F-v1.0 §3]
- The 30 task-statement titles are identical between v0.1 and v1.0 (only line wrapping differs). The v1.0 document-control table describes v1.0 as "Formatting and layout updates" over a June 2026 v0.2 draft. [source: OG-F-v0.1 and OG-F-v1.0, diff of "Task Statement" lines; OG-F-v1.0 §18]
- The repo's "Examples of Exam Questions" section reproduces the 12 sample questions from the official guide in paraphrased form (both have 12; same scenarios and correct answers). [source: guide_en.md "Examples of Exam Questions"; OG-F-v0.1 sample questions]
- The repo's "4 out of 8 possible scenarios" claim is not official. The official guides say 4 scenarios drawn from a bank of 6. Scenarios 7 ("Conversational AI Architecture Patterns") and 8 ("Agentic AI Tools", empty) come from candidate reports. [source: guide_en.md "Exam Scenarios"; OG-F-v1.0 §5] Whether these scenarios appear on live forms is [unverified].

### 4. Domain structure, weights, and task statements it uses

The repo uses the official 5-domain Foundations blueprint and all 30 task statements. [source: guide_en.md Part II; OG-F-v1.0 §4, §6]

| Domain | Weight | Task statements (repo Part II headings) |
|---|---|---|
| 1. Agentic Architecture & Orchestration | 27% | 1.1 agentic loops · 1.2 coordinator-subagent orchestration · 1.3 subagent invocation, context passing, spawning · 1.4 multi-step workflows with enforcement and handoff · 1.5 Agent SDK hooks · 1.6 task decomposition · 1.7 session state, resume, fork |
| 2. Tool Design & MCP Integration | 18% | 2.1 tool interfaces and descriptions · 2.2 structured MCP error responses · 2.3 tool distribution and `tool_choice` · 2.4 MCP servers in Claude Code and agents · 2.5 built-in tools (Read, Write, Edit, Bash, Grep, Glob) |
| 3. Claude Code Configuration & Workflows | 20% | 3.1 CLAUDE.md hierarchy and modularity · 3.2 slash commands and skills · 3.3 path-specific rules · 3.4 plan mode vs direct execution · 3.5 iterative refinement · 3.6 CI/CD integration |
| 4. Prompt Engineering & Structured Output | 20% | 4.1 explicit criteria · 4.2 few-shot · 4.3 `tool_use` + JSON schemas · 4.4 validation/retry/feedback loops · 4.5 batch processing · 4.6 multi-instance and multi-pass review |
| 5. Context Management & Reliability | 15% | 5.1 preserving critical context · 5.2 escalation and ambiguity · 5.3 error propagation · 5.4 large-codebase context · 5.5 human review and confidence calibration · 5.6 provenance and uncertainty |

- Official scenarios (bank of 6): Customer Support Resolution Agent, Code Generation with Claude Code, Multi-Agent Research System, Developer Productivity with Claude, Claude Code for CI, Structured Data Extraction. [source: OG-F-v1.0 §5]
- Exam facts from the official guide: 60 items, 120 minutes, scaled score 100–1,000 with 720 to pass, $125 fee, 12-month validity. [source: OG-F-v1.0 §3]

### 5. Anki decks: format and build

- Each language has one `.apkg` file. The English deck has **60 notes and 60 cards** (one card per note), with 15 cards per scenario across 4 scenarios. [source: REPO anki/practical_test_en.apkg, SQLite inspection of `notes`/`cards`]
- The note type is "Claude Certified Architect MCQ" with 9 fields: `Scenario`, `Situation`, `Question`, `OptionA`–`OptionD`, `Correct`, `Explanation`. The front shows scenario, situation, question, and an A–D list. The back shows "Answer: <letter>" plus the explanation. [source: utils/build_anki_deck.py `_MODEL`, `_FRONT`, `_BACK`]
- Each note is tagged with the language and a scenario slug (for example `customer-support-agent`). The deck name is `Claude Certified Architect :: <lang>`, and the deck ID is derived from a SHA-256 of the language. [source: utils/build_anki_deck.py `build_deck`, `_deck_id`]
- Build pipeline: `genanki` parses the `const QUESTIONS = [...]` JSON array embedded in `practical_test_<lang>.html`, validates that A–D are present, and writes `anki/practical_test_<lang>.apkg`. A GitHub Action runs on pushes that touch `practical_test_*.html` and commits the decks back. `anki/.source-hash` skips unchanged languages. [source: utils/build_anki_deck.py; .github/workflows/html-to-anki.yml]
- The HTML builder calls `extract_question.py`, but that script is not in the repo. Regenerating the HTML from the markdown is not reproducible from the repo alone. [source: utils/build_practical_test_html.py `get_questions`; REPO file tree]
- The deck covers only questions 1–60. The 16 "Conversational AI" questions (61–76) exist only in the markdown guide. [source: practical_test_en.html QUESTIONS array length = 60; guide_en.md Q61–Q76]
- The correct-answer letters in the 60-item bank are spread as A 18, B 15, C 13, D 14. [source: practical_test_en.html QUESTIONS array, counted]

### 6. Highest-yield technical content (by topic)

#### Agentic loop and `stop_reason`
- Loop rule: continue while `stop_reason == "tool_use"` (run the tool, append a `tool_result`, call again). Stop on `"end_turn"`. [source: guide_en.md §3.1; OG-F-v1.0 Task 1.1]
- Anti-patterns the exam names: parsing assistant text for "done", using an arbitrary iteration cap as the primary stop condition, and treating "assistant produced text" as completion. [source: guide_en.md §3.1; OG-F-v1.0 Task 1.1]
- The API is stateless. Every request must resend the full `messages` history. "Claude forgot what I said two turns ago" means the app dropped prior messages. [source: guide_en.md §1.1, Q64]
- Tool results go back as a `tool_result` block inside a `user`-role message. No `tool` role exists. [source: guide_en.md §1.2]
- The repo lists four `stop_reason` values (`end_turn`, `tool_use`, `max_tokens`, `stop_sequence`). [source: guide_en.md §1.3] Current docs list seven, adding `pause_turn` (server-tool loop hit its 10-iteration default), `refusal`, and `model_context_window_exceeded`. [source: https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons]

#### Orchestration and subagents
- Hub-and-spoke: the coordinator owns decomposition, delegation, aggregation, error handling, and routing. All inter-agent traffic goes through it for observability. [source: guide_en.md §3.3; Practice Q2, Q8]
- Subagents do not inherit the coordinator's history. Everything the subagent needs must go in the prompt passed to it. [source: guide_en.md §3.3–3.4; OG-F-v1.0 Task 1.2] Current SDK docs confirm this: "The only content you pass from parent to subagent is the Agent tool's prompt string." [source: https://code.claude.com/docs/en/agent-sdk/subagents]
- Exam vocabulary: subagents are spawned via the `Task` tool, and the coordinator's `allowedTools` must include `"Task"`. Multiple `Task` calls in one response run in parallel. [source: guide_en.md §3.4; OG-F-v1.0 Appendix]
- An overly narrow decomposition is a root-cause pattern. "Creative industries" split only into visual-art subtopics leads to reports that miss music, literature, and film. [source: Practice Q4]
- Partition the research space before delegating (distinct subtopics or source types) to avoid duplicate work. [source: Practice Q11]
- Least-privilege fix for the synthesis agent: give it a scoped `verify_fact` tool for the 85% of simple checks, and keep complex verification routed through the coordinator. [source: Practice Q15]

#### Hooks and programmatic enforcement
- `PostToolUse` normalizes tool output before the model sees it. Examples: Unix timestamps to ISO 8601, numeric status codes to labels, trimming 40+ fields to 5. This works for third-party MCP servers you cannot modify. [source: guide_en.md §3.5, §11.2; Practice Q59]
- A `PreToolUse` interception hook blocks policy violations, such as a refund above $500, and redirects to escalation. [source: guide_en.md §3.5; OG-F-v1.0 Task 1.5]
- Decision rule: hooks and preconditions give deterministic guarantees, while prompts give probabilistic compliance. Use code when failure has financial, legal, or safety impact. [source: guide_en.md §3.5; OG-F-v1.0 Task 1.4]. The repo's ">90%" figure for prompt compliance has no source. [unverified]
- Canonical item: in 12% of cases the agent skips `get_customer`. The fix is a programmatic precondition that blocks `lookup_order`/`process_refund` until a verified ID exists. Prompt changes, few-shot examples, and a routing classifier are the distractors. [source: guide_en.md Example Q1; OG-F-v1.0 §9 Q1]
- The repo uses a pseudo-API (`@hook("PostToolUse")`). The real SDK takes callbacks in `options.hooks` with a `matcher`. `PreToolUse` blocks by returning `permissionDecision: "deny"`. `PostToolUse` replaces output with `updatedToolOutput`. When multiple hooks apply, `deny` beats `defer`, `ask`, and `allow`. [source: https://code.claude.com/docs/en/agent-sdk/hooks]

#### Tool design and `tool_choice`
- The tool description is the primary selection mechanism. When tools are confused, the first fix is to expand descriptions with input formats, example queries, edge cases, and "use this vs that" boundaries. Few-shot examples, a routing layer, and merging tools are the distractors. [source: guide_en.md §2.2; Example Q2; OG-F-v1.0 §9 Q2]
- Renaming removes overlap, for example `analyze_content` to `extract_web_results`. Replacing a generic `fetch_url` with a constrained `load_document` stops misuse. [source: Practice Q7, Q10; OG-F-v1.0 Task 2.1, 2.3]
- Too many tools per agent (18 instead of 4–5) degrades selection. Scope each agent to role-relevant tools. [source: guide_en.md Domain 2.3; OG-F-v0.1 Task 2.3]
- Keyword-sensitive system-prompt wording, such as "always verify the customer" or the word "account", creates unintended tool associations. [source: guide_en.md §1.4; Practice Q56]
- `tool_choice` options in exam terms: `auto` (may answer in text), `any` (must call some tool), `{"type":"tool","name":...}` (must call that tool, used to force a first step such as `extract_metadata`). [source: guide_en.md §2.3; OG-F-v1.0 Task 2.3]
- A destructive operation with preview should be split into two tools: `preview_*` returns a single-use token, and `execute_*` requires it. A `dry_run` flag plus instructions is the weaker option. [source: guide_en.md Q61]

#### MCP
- MCP primitives: tools (actions), resources (read-only context such as catalogs and schemas, which reduce exploratory calls), and prompts (templates). [source: guide_en.md §4.1, §4.5]
- Scope: project `.mcp.json` (committed, shared, secrets via `${GITHUB_TOKEN}` env expansion) vs user `~/.claude.json` (personal or experimental). Tools from all connected servers are available at the same time. Prefer community servers for standard integrations. [source: guide_en.md §4.3; Practice Q44; OG-F-v1.0 Task 2.4]
- Errors: return `isError: true` with structured content (`errorCategory` transient/validation/business/permission, `isRetryable`, message, attempted query, partial results). "Operation failed" is the anti-pattern. [source: guide_en.md §4.4, §10.1; OG-F-v0.1 Task 2.2]
- Distinguish an access failure (timeout, needs a retry decision) from a valid empty result ("0 results" is a successful query). [source: Practice Q12]
- Retry transient errors inside the tool with backoff, and return non-retryable syntax errors immediately with validation details. This beats returning a `retryable` flag for the agent to interpret. [source: guide_en.md Q62]
- Gap: the repo does not cover MCP transports. The current spec (2025-11-25) defines stdio and Streamable HTTP. Streamable HTTP replaces the HTTP+SSE transport from 2024-11-05. [source: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

#### Claude Code configuration
- CLAUDE.md levels in exam terms: user `~/.claude/CLAUDE.md` (not shared), project `CLAUDE.md` or `.claude/CLAUDE.md` (in VCS), and subdirectory CLAUDE.md. Classic item: a new hire misses a rule because it lives in teammates' user-level files. [source: guide_en.md §5.1; Practice Q37]
- Current docs add a managed-policy CLAUDE.md (org-wide, cannot be excluded) and `CLAUDE.local.md` (personal, gitignored). Ancestor files load at launch and subdirectory files load on demand. [source: https://code.claude.com/docs/en/memory]
- `@path` imports resolve relative to the importing file. The repo says max depth is 5. [source: guide_en.md §5.2] Current docs say "a maximum depth of four hops". [source: https://code.claude.com/docs/en/memory]
- `.claude/rules/*.md` with a YAML `paths:` glob list loads only when Claude touches matching files. Use it for conventions spread across directories (`**/*.test.tsx`) instead of per-directory CLAUDE.md. [source: guide_en.md §5.3; Practice Q40, Q42] Docs confirm `paths` is the only frontmatter field read from a rule. [source: https://code.claude.com/docs/en/memory]
- Skills frontmatter tested on the exam: `context: fork` (isolated subagent, stops verbose output from polluting the session), `allowed-tools` (restricts tools), `argument-hint` (prompts for missing args). [source: guide_en.md §5.5; Practice Q35, Q39, Q43; OG-F-v1.0 Appendix]
- Put on-demand workflows (PR review, deploy, migrations) in skills and keep always-on standards in CLAUDE.md. [source: Practice Q33, Q38]
- Team `/review` command location: `.claude/commands/` in the repo. Distractors include `~/.claude/commands/`, root CLAUDE.md, and a nonexistent `.claude/config.json`. [source: Example Q4; Practice Q41]
- Plan mode is for multi-file, architectural, or ambiguous work (microservice split, 45+ file migration, choosing among Slack integration styles). Direct execution is for a single-file fix with a clear stack trace. Use an Explore subagent to isolate verbose discovery. [source: guide_en.md §5.6; Practice Q32, Q34, Q45]
- CI: `claude -p` (`--print`) runs non-interactively. `--output-format json --json-schema '<schema>'` produces structured findings for inline PR comments. Distractors include `CLAUDE_HEADLESS=true`, `--batch`, and redirecting stdin from `/dev/null`. [source: Example Q10; Practice Q16, Q26] Docs: schema-conformant output lands in the `structured_output` field, and `--bare` is recommended for scripted runs. [source: https://code.claude.com/docs/en/headless]
- Use an independent review instance without the generator's context. Feed prior findings back on re-review and report only new or unresolved issues. Include existing tests in context to avoid duplicate test suggestions. [source: guide_en.md §5.9; Practice Q17, Q24, Q25]
- Sessions: `--resume` continues a session, and `fork_session` branches from shared context. Start fresh with a summary when tool results are stale. [source: guide_en.md §5.10] In the SDK, fork means `resume=<id>` plus `fork_session=True` (Python) or `forkSession: true` (TS). [source: https://code.claude.com/docs/en/agent-sdk/sessions]

#### Prompt engineering, structured output, validation
- Explicit categorical criteria beat "be conservative". For example: flag a comment only if it contradicts code behavior. [source: guide_en.md §6.2; Practice Q22]
- When some categories have high false-positive rates (style 52%, docs 48% vs security 8%), temporarily disable them to restore trust. [source: Practice Q29]
- Few-shot: 2–4 targeted examples for ambiguous cases, each with rationale. Few-shot is the strongest lever for consistent output format. [source: guide_en.md §6.1; OG-F-v0.1 Task 4.2; Practice Q20, Q60]
- `tool_use` with a JSON schema removes syntax errors but not semantic ones (totals that do not add up, values in the wrong field). [source: guide_en.md §2.4–2.5; OG-F-v1.0 Task 4.3]
- Schema rules: mark fields required only if always present, use nullable `["string","null"]` to prevent fabrication, and add enum `"other"` + detail string and `"unclear"`. [source: guide_en.md §2.4]
- Validate–retry loop: resend the original document, the bad extraction, and the specific error. Retry fails when the data is absent from the source. Extract `stated_total` and `calculated_total` to detect conflicts. [source: guide_en.md §6.5–6.6; OG-F-v1.0 Task 4.4]

#### Message Batches API
- Exam facts: 50% cost savings, up to 24 h processing, no latency SLA, no multi-turn tool calling within a request, `custom_id` for correlation, resubmit only failed IDs. [source: guide_en.md §7.1–7.4; OG-F-v0.1 Task 4.5]
- Decision rule: blocking pre-merge checks stay synchronous. Overnight reports and weekly audits go to batch. [source: Example Q11; Practice Q19, Q21, Q30]
- SLA arithmetic: a 30 h SLA with 24 h processing implies 4 h submission windows. [source: guide_en.md §7.5; OG-F-v0.1 Task 4.5]
- Extra limits from current docs: 100,000 requests or 256 MB per batch, most batches finish within 1 h, results kept 29 days, results may come back out of order, `custom_id` must match `^[a-zA-Z0-9_-]{1,64}$`, and prompt-cache hits are best-effort. [source: https://platform.claude.com/docs/en/build-with-claude/message-batches]

#### Context management, escalation, errors, provenance
- Extract transactional facts (amounts, dates, IDs) into a persistent "case facts" block outside summarized history, because progressive summarization blurs numbers. [source: guide_en.md §11.1; Practice Q54]
- Lost-in-the-middle mitigation: put a key-findings summary first and use explicit section headings. [source: guide_en.md §11.3; Practice Q13]
- Make upstream agents return structured facts, quotes, and scores instead of raw pages and reasoning (155K tokens into a synthesizer that works best under 50K). [source: Practice Q14]
- Escalation triggers: an explicit human request (honor immediately), a policy gap (competitor price match), or no progress. Sentiment and self-rated confidence are unreliable. Multiple customer matches call for asking for another identifier. [source: guide_en.md §9.1; Practice Q49, Q50, Q55]
- Handoff to a human is a structured, self-contained summary (customer ID, root cause, actions taken, recommended action), because the operator does not see the transcript. [source: guide_en.md §9.3]
- Error anti-patterns: a generic "unavailable" status, silent suppression (empty = success), aborting the whole workflow, and infinite subagent retries. Recover locally, then propagate with partial results, and annotate coverage gaps in the synthesis. [source: guide_en.md §10.2–10.4; Practice Q3, Q5]
- Aggregate accuracy (97%) can hide failures by document type. Use stratified sampling and field-level confidence calibrated on labeled sets. [source: guide_en.md §9.4; OG-F-v0.1 Task 5.5]
- Provenance: keep claim→source mappings (URL, date) and preserve conflicting values with attribution for the coordinator to reconcile. Dates prevent temporal differences from reading as contradictions. [source: guide_en.md §12.1–12.3; Practice Q1]

#### Prompt caching
- The repo covers prompt caching only as "beyond knowing it exists" (out of scope for Foundations). [source: guide_en.md "Out-of-Scope Topics"; OG-F-v1.0 Appendix]
- Professional tests it directly: one sample question answers "place the static system prompt and policy before the dynamic content and enable prompt caching". [source: OG-P-v1.0 §8 Sample 2]
- Current docs add mid-conversation `role: "system"` messages, which preserve the cached prefix. The repo describes this feature correctly. [source: guide_en.md §1.2; https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages]

### 7. Exam-vs-current-docs drift instructors should flag

| Topic | Exam / repo wording | Current docs (2026-10-13) |
|---|---|---|
| Subagent tool | `Task` tool; `allowedTools` includes `"Task"` [source: OG-F-v1.0 Appendix] | `Agent` tool in `tool_use` blocks since Claude Code v2.1.63; still listed as `"Task"` in `system:init` [source: https://code.claude.com/docs/en/agent-sdk/subagents] |
| `AgentDefinition` fields | `name`, `system_prompt`, `allowed_tools` [source: guide_en.md §3.2] | `description`, `prompt`, `tools`, `model`, `maxTurns`, ...; the name is the `agents` dict key [source: https://code.claude.com/docs/en/agent-sdk/subagents] |
| Forced `tool_choice` | `any` / forced tool guarantees structured output [source: OG-F-v1.0 Task 4.3] | `any` and `tool` return 400 on Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1; use `auto` + strict tool use or structured outputs [source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use; https://platform.claude.com/docs/en/models/opus-5-5/migration-guide] |
| Assistant prefill | Q72 answer: "Append a partial assistant message" [source: guide_en.md Q72] | Prefill returns 400 on Opus 4.6 and later Opus models [source: https://platform.claude.com/docs/en/models/opus-5-5/migration-guide] |
| Personal skill override | Official task 3.2: personal variants "with different names" [source: OG-F-v0.1 Task 3.2] | Repo changed Q36 to "same name shadows project" on 2026-09-09, citing docs precedence enterprise > personal > project [source: REPO PR #50; https://code.claude.com/docs/en/skills] |
| `@import` depth | 5 [source: guide_en.md §5.2] | four hops [source: https://code.claude.com/docs/en/memory] |
| Commands vs skills | `.claude/commands/` for slash commands [source: OG-F-v1.0 Appendix] | Commands merged into skills; both create `/name` [source: https://code.claude.com/docs/en/skills] |
| Model IDs | `claude-sonnet-4-6`, `claude-opus-4-6`, `claude-haiku-4-5` [source: guide_en.md §1.1] | Docs examples use `claude-opus-5-5` [source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use] |

### 8. Question style

- All items are scenario-anchored and single-answer with four options (A–D). Each item has a "Situation" stem, usually with production metrics ("12% of cases", "45% of the time", "55% vs 80% target"), and a prompt such as "most effective first step" or "most likely root cause". [source: guide_en.md Practice Test; practice_test_en.html]
- The README tells readers to find the deciding phrase ("most effective **first** step"), prefer the proportionate root-cause fix with the least new machinery, and choose programmatic enforcement over stronger prompts when a rule must always hold. [source: REPO README.md "How to Read the Practical Test Questions"]
- Recurring distractor types: (1) a prompt or few-shot fix where a deterministic guarantee is needed; (2) over-engineering (classifier, routing layer, dedicated error agent); (3) masking failure (empty result marked success, generic error, aggregate metric); (4) "bigger model or larger context"; (5) shifting burden to developers or users; (6) nonexistent features (`CLAUDE_HEADLESS`, `--batch`, `override: true`, `.claude/config.json`, `session_id` parameter). This taxonomy is my own synthesis of the 76 items. [source: guide_en.md Practice Test Q1–Q76]
- The README states that the practice questions "come from the real exam materials and are kept as they are". [source: REPO README.md] The official guide says its samples are "drawn from the practice test", and the repo's Q51/Q57 match official samples 1–2 closely. This makes the 60 items likely near-copies of Anthropic's official practice exam. [source: OG-F-v0.1 sample-question intro; guide_en.md Q51, Q57] The exact wording differs slightly, which suggests re-translation. [unverified]

Representative items are not reproduced here. The repo says its practice items come from official exam materials, so this course writes its own questions instead. Typical shapes: error propagation in multi-agent research (timeout vs. valid empty result), why batch processing fails for iterative tool-calling workflows, personal vs. project skill precedence, and binding a destructive tool call to a confirmed preview token.

### 9. Other community resources

| Repo | Stars / last push | Exam | What it covers |
|---|---|---|---|
| [daronyondem/claude-architect-exam-guide](https://github.com/daronyondem/claude-architect-exam-guide) | 1,116 / 2026-06-10 | Foundations | One long guide (~2,265 lines) in 11 knowledge areas, each with "What to Know" and "Common Pitfalls". It is more current on API details than paullarionov: `output_config.format` structured outputs, prefill as legacy, MCP protocol errors vs tool-execution errors, uncertain side effects on write timeouts. No question bank. [source: daronyondem README.md, exam-preparation-guide.md §1, §3] |
| [dnacenta/claude-certified-architect](https://github.com/dnacenta/claude-certified-architect) | 129 / 2026-09-26 | Foundations deep-dive, plus overviews of CCAR-P, CCDV-F, CCAO-F | Per-domain files (`domains/d1…d5`) and `certs/ccar-p-architect-professional.md`, which summarizes the v1.0 Professional blueprint, the delta topics (RAG, evals/A/B, regulated compliance, stakeholder lifecycle), and links the official PDFs. [source: dnacenta certs/ccar-p-architect-professional.md] |
| [sarveshtalele/claude-architect-exam-guide](https://github.com/sarveshtalele/claude-architect-exam-guide) | 176 / 2026-09-12 | Foundations and Professional | Copies of both official v1.0 exam guide PDFs, a Claude Code study skill with `/ccarf-*` commands (diagnostic, drill, mock, weekly plan, score check), and copy-paste prompt packs for learning, practice, and mock tests. No original question bank. [source: sarveshtalele README.md; foundations/ccar-f-examprep-coach/; professional/] |
| [juanmartincoma-collab/claude-certified-architect-es](https://github.com/juanmartincoma-collab/claude-certified-architect-es) | 2 / 2026-08-11 | Foundations and **Professional** | Spanish-language reasoning guides with English questions. It has a 60-item CCAR-F mock and a **63-item CCAR-P mock**, where 25 CCAR-P items are multiple-response ("Selecciona 2"), matching the v1.0 format. The CCAR-P guide covers model selection and routing, prompt caching, least privilege, deterministic gates, RAG chunking/indexing/retrieval, MCP vs API/CLI vs agent-to-agent, progressive discovery, and observability. The author says they passed CCAR-P in August 2026 and that all questions are original. [source: juanmartincoma README.en.md; profesional/guia.md; profesional/examen.md] The README's "163 original questions" total does not match the 123 items in the two exam files. [unverified] |

- The Professional blueprint has 7 domains: Solution Design & Architecture 17%, Models/Prompting/Context Engineering 13%, Integration 19%, Evaluation/Testing/Optimization 16%, Governance/Safety/Risk 14%, Stakeholder Communication & Lifecycle 14%, Developer Productivity & Operational Enablement 7%. It has 63 items, 120 minutes, 720/1,000 to pass, and a $175 fee. [source: OG-P-v1.0 §5–6]

## Comparison

How far paullarionov (Foundations) content reaches into the Professional blueprint:

| CCAR-P domain | Weight | paullarionov coverage | Best community supplement |
|---|---|---|---|
| 1 Solution Design & Architecture | 17% | Partial: multi-agent orchestration, decomposition. No workflow vs agentic vs augmented-LLM pattern selection and no business-value alignment. [source: guide_en.md Ch. 3, 8; OG-P-v1.0 §6] | juanmartincoma profesional/guia.md Dominio 1 |
| 2 Models, Prompting & Context Engineering | 13% | Partial: few-shot, explicit criteria, context trimming. No model selection and no caching. [source: guide_en.md Ch. 6, 11] | juanmartincoma Dominio 2 |
| 3 Integration | 19% | Partial: MCP config, tool scoping, least privilege. No RAG, authn/authz, observability, or MCP vs A2A. [source: guide_en.md Ch. 2, 4] | juanmartincoma Dominio 3; dnacenta CCAR-P overview |
| 4 Evaluation, Testing & Optimization | 16% | Thin: stratified sampling and false-positive tuning only. [source: guide_en.md §9.4; Practice Q29] | None strong |
| 5 Governance, Safety & Risk | 14% | Thin: escalation and human-in-the-loop only. No GDPR/HIPAA/FedRAMP and no bias. [source: guide_en.md Ch. 9] | juanmartincoma (partial) |
| 6 Stakeholder Communication & Lifecycle | 14% | None. [source: guide_en.md full outline] | juanmartincoma (partial) |
| 7 Developer Productivity & Enablement | 7% | Strong: CLAUDE.md, rules, skills, CI, plan mode. [source: guide_en.md Ch. 5, 13] | paullarionov itself |

## Open questions

- **IP risk.** The repo says its 60 practice items come from official practice materials. This course paraphrases topics only and writes original questions.
- **Q36 key conflict.** The official task statement favors "different name" (A). The repo now keys C. Which answer should course flashcards teach for exam purposes?
- **Docs drift.** Should course materials teach exam vocabulary (`Task`, forced `tool_choice`, prefill) with a "current docs differ" callout, or current APIs first?
- **Conversational AI scenario.** Is it worth drilling Q61–Q76 when that scenario is not in the official bank of 6 for Foundations and Professional has no published scenarios?
