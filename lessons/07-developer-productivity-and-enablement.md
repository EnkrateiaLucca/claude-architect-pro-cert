# Lesson 7: Developer Productivity & Operational Enablement

**Exam domain:** D7 (7%, ~4 items) · **Time in session:** Segment 4, about 6 minutes

## What the exam asks

Verbatim objectives from the Exam Guide:

- Configure Claude tools and environments for teams (e.g., Claude Code)
- Improve developer workflows using AI-assisted tooling
- Support debugging and operational issue resolution

The official prep course frames D7 as running a live system "without depending on you": shared configuration, a rollout pattern, a Skills distribution strategy, spend controls, review discipline for AI-generated work, and a team that resolves issues on its own.

## Key ideas

### Which layer does a setting belong at?

Claude Code reads configuration from several scopes. The exam tests whether you put each setting at the right one.

| Scope | File | Shared? | Put here |
|---|---|---|---|
| **Managed (enterprise)** | `managed-settings.json` (file, MDM, or server-managed), managed policy `CLAUDE.md` | Org-wide, **cannot be overridden** | Security policy: denied tools, MCP allowlist, marketplace restrictions, disabling bypass mode, telemetry |
| **Project (shared)** | `.claude/settings.json`, `CLAUDE.md`, `.mcp.json`, `.claude/skills/`, `.claude/agents/` | Committed to git | Team conventions, project permissions, hooks, project MCP servers |
| **Project (local)** | `.claude/settings.local.json`, `CLAUDE.local.md` | Gitignored | One developer's overrides for this repo |
| **User** | `~/.claude/settings.json`, `~/.claude/CLAUDE.md` | Personal | Personal preferences across all repos |

Precedence runs managed → command-line flags → local project → shared project → user. Permission rules evaluate **deny → ask → allow**: an allow rule can't carve an exception out of a deny. Permission modes range from `default` (ask) and `plan` (read-only) to `acceptEdits`, `auto`, and `bypassPermissions`; managed settings can disable the risky ones. A team convention in someone's user file never reaches the rest of the team; a security rule in a project file can be overridden by a managed setting only.

### Guidance vs. enforcement

| Mechanism | Nature | Use for |
|---|---|---|
| `CLAUDE.md` | Guidance (instructions in context) | Conventions, commands, architecture notes |
| **Permissions** (allow / ask / deny) | Enforced | Which tools and commands may run |
| **Hooks** (e.g., `PreToolUse`, `PostToolUse`) | Enforced, deterministic (exit code 2 blocks the action) | Block a command, run the formatter, run tests after edits |
| **Managed settings** | Enforced org-wide | Policy that no developer can turn off |

If a rule must always hold, it belongs in permissions, hooks, or managed settings. A line in `CLAUDE.md` is best effort. This is the D7 version of the exam-wide rule: enforce in code, not in the prompt.

### Rollout and distribution

- **Pilot → shared config → champions → wider rollout.** Start with one team, commit the working configuration to the repo, measure, then expand.
- **Skills** package reusable know-how (`SKILL.md` + scripts + references). They load by **progressive disclosure**: only the name and description sit in context until the skill is needed.
- **Plugins** bundle skills, slash commands, subagents, hooks, and MCP servers for distribution through a **plugin marketplace**. Managed settings can restrict which marketplaces and MCP servers are allowed.
- **Spend controls** belong in team setup: workspace or organization spend limits, per-user limits on Team/Enterprise plans, and usage monitoring (OpenTelemetry export, the analytics dashboard, the Claude Code Analytics API). Anthropic's budgeting baseline is roughly $150–250 per developer per month across enterprise deployments.
- **Lock-down options** for regulated orgs: managed-only permission rules, hooks, and MCP servers; `strictKnownMarketplaces` / `blockedMarketplaces`; and `forceRemoteSettingsRefresh`, which refuses to start a session if org policy can't be fetched (fail closed).

### Developer workflows

| Workflow | How |
|---|---|
| Explore → plan → code → commit | **Plan mode** for read-only exploration before edits |
| CI and automation | **Headless mode** `claude -p "<task>"`, with `--output-format json`, scoped `--allowedTools` |
| PR review and issue triage | Claude Code **GitHub Actions** (`@claude` mentions) |
| Repeated team procedures | Skills and custom slash commands in the repo |
| Specialized helpers | **Subagents** in `.claude/agents/` with their own tools and context |

**Review discipline.** AI-generated code passes the same gates as human code: tests, linters, human PR review. Use an **independent** review pass (a fresh session or a separate reviewer instance). The session that wrote the code shares its blind spots.

### Debugging and operational issue resolution

Connect the symptom to an architectural cause before changing anything:

| Symptom | Likely cause | First action |
|---|---|---|
| Claude ignores a team convention | Rule lives in a user file, or is buried in a long `CLAUDE.md` | Move to project `CLAUDE.md`; enforce with a hook if critical |
| An MCP tool works for one developer only | Server configured at user or local scope | Move to project `.mcp.json` |
| A developer runs a forbidden command | Rule was guidance, not enforcement | Add a deny permission or a managed setting |
| Costs spike for one team | No spend limit, or long sessions without compaction | Set limits, monitor OTel usage, coach on `/clear` and `/compact` |
| Production agent errors after a change | Change shipped without evals | Roll back, run the eval suite, then re-ship |

Build the team toward self-sufficiency: runbooks for common failures, a shared eval command, and named owners. Escalation to the architect is the exception.

## Exam traps

- **Security policy in `CLAUDE.md`.** Instructions are not enforcement. Use permissions, hooks, or managed settings.
- **Team config in user scope.** It never reaches teammates. Commit it to the project.
- **The author reviews its own code.** Use an independent reviewer.
- **Big-bang rollout.** Pilot, measure, then expand.

## Exercise

`exercises/07-team-config.md`: place ten settings at the right scope and choose guidance or enforcement for each.

## Check yourself

1. Security wants every developer blocked from `rm -rf` and from unapproved MCP servers, with no opt-out. Where?
2. The team wants Claude to always run `npm test` after editing files. `CLAUDE.md` or a hook?
3. A GitHub workflow should run Claude on each PR without a human at the keyboard. Which mode?

<details>
<summary>Answers</summary>

1. Managed settings (enterprise policy), which developers cannot override.
2. A `PostToolUse` hook. "Always" means deterministic.
3. Headless mode (`claude -p`), typically through the Claude Code GitHub Action.

</details>

## Official resources

- Claude Code settings: https://code.claude.com/docs/en/settings
- Claude Code memory (CLAUDE.md): https://code.claude.com/docs/en/memory
- Hooks: https://code.claude.com/docs/en/hooks
- Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Managed settings and admin setup: https://code.claude.com/docs/en/admin-setup
- GitHub Actions: https://code.claude.com/docs/en/github-actions
- Official prep course 5, Team Enablement & Operational Productivity: https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional
