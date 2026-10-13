# Claude Certified Architect – Professional (CCAR-P): Exam Prep

Course materials for the O'Reilly live training *Claude Certified Architect – Professional Exam Prep*. The official [Exam Guide v1.0](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf) is the compass for everything here.

## What's inside

| Path | What it is |
|---|---|
| `study-guide.html` | The whole course on one page: blueprint, domain lessons, all 60 practice questions, exercises, strategy, quick reference, and resources. Open in a browser. |
| `exam-guide.html` | Interactive companion to the official exam guide: blueprint self-assessment, official sample questions, and exam policies |
| `presentation/claude-architect-pro-exam-prep.html` | Live slide deck (remark.js). Open in a browser; press `P` for presenter notes. |
| `presentation/claude-architect-pro-exam-prep.pdf` | PDF export of the slide deck |
| `lessons/` | One markdown lesson per exam domain, with verbatim objectives, decision tables, traps, and self-checks |
| `exercises/` | Eight hands-on exercises (design drills with reference answers) plus two runnable scripts in `exercises/scripts/` |
| `questions/practice-questions.md` | 60 original exam-style questions weighted by domain, with answers and distractor analysis |
| `questions/quiz.html` | The same 60 questions as a click-to-check quiz with a score tracker and domain filter |
| `questions/questions.json` | The question database (source of truth) |
| `anki/ccar-p-flashcards.apkg` | 60 Anki flashcards, tagged by domain. Import with **File → Import** |
| `anki/flashcards.csv` | Flashcard source (also importable into other tools) |
| `cheatsheet/ccar-p-cheatsheet.pdf` | Five-page printable cheatsheet of the whole course |
| `research/` | Sourced research notes behind the materials |
| `build.py` | Rebuilds the markdown bank, quiz, and Anki deck: `uv run build.py` |

## Schedule (120 min)

| Segment | Time | Exam domains | Lessons |
|---|---|---|---|
| 1. The exam and solution design | 25 min | Blueprint + D1 (17%) | `00`, `01` |
| 2. Models, context, and integration | 35 min | D2 (13%) + D3 (19%) | `02`, `03` |
| 3. Evaluation and governance | 30 min | D4 (16%) + D5 (14%) | `04`, `05` |
| 4. Stakeholders and team enablement | 20 min | D6 (14%) + D7 (7%) | `06`, `07` |
| 5. Exam strategy and study plan | 10 min | All | `08` |

## Exam at a glance

Exam code CCAR-P · 63 items · 120 minutes · scaled score 720/1,000 to pass · $175 · Pearson VUE (online or test center) · valid 12 months, free on-time renewal · no prerequisites. Registration currently requires a Claude Partner Network company email.

## Exercises

| # | Exercise | Domain |
|---|---|---|
| 00 | Walk the three official samples | All |
| 01 | Ownership, shape, pattern for five business problems | D1 |
| 02 | Break and fix prompt caching (`scripts/prompt_caching.py`) + context strategy | D2 |
| 03 | Integration design review: seven flaws | D3 |
| 04 | Eval plan + mixed-method harness (`scripts/eval_harness.py`) | D4 |
| 05 | Place the safety stack for a loan assistant | D5 |
| 06 | Discovery role-play + one-page ADR | D6 |
| 07 | Put each Claude Code setting at the right layer | D7 |

The scripts use [uv](https://docs.astral.sh/uv/) inline metadata and need `ANTHROPIC_API_KEY`. `uv run exercises/scripts/eval_harness.py --selftest` runs offline.

## Before the session

1. Clone this repo.
2. Optional: an Anthropic API key to run the two scripts (a few cents each).
3. Optional: Anthropic's five-course [official prep path](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional) (Partner Academy) and the free [Anthropic Academy](https://anthropic.skilljar.com/) courses on the Claude API, MCP, and Claude Code.

Practice questions and flashcards are original and are not drawn from the live exam. Platform facts (models, pricing, feature eligibility) were checked against Anthropic's documentation in October 2026 and will change; the exam objectives test the reasoning, not the version numbers.
