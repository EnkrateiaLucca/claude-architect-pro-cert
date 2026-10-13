# Exercise 7: Put Each Setting at the Right Layer

**Lesson:** 07 · **Time:** 10 minutes · **Format:** sorting drill

For each item, choose the **scope** (managed · project shared · project local · user) and the **mechanism** (CLAUDE.md guidance · permission rule · hook · MCP config · skill/plugin · spend/telemetry setting).

1. Block `curl` to external hosts for every engineer in the company, no opt-out.
2. "Use pnpm, not npm" for this repo.
3. Run the formatter after every file edit in this repo.
4. A teammate prefers a more verbose output style.
5. Connect the team's Jira MCP server for this repo, with the token read from an environment variable.
6. Only MCP servers on an approved list may be used anywhere in the company.
7. A repeatable "release notes" procedure the whole platform team uses across 14 repos.
8. One developer temporarily allows `docker compose` without prompting while debugging.
9. Org-wide monthly usage limits and usage dashboards.
10. Never edit files under `migrations/` without asking.

<details><summary>Reference answers</summary>

| # | Scope | Mechanism | Why |
|---|---|---|---|
| 1 | Managed | Permission deny rule | Security policy with no opt-out |
| 2 | Project shared | `CLAUDE.md` | Team convention; guidance is enough |
| 3 | Project shared | `PostToolUse` hook | "Every" edit means deterministic |
| 4 | User | User settings | Personal preference |
| 5 | Project shared | `.mcp.json` with `${ENV_VAR}` | Shared server, secret stays out of git |
| 6 | Managed | MCP allowlist | Org-wide enforcement |
| 7 | Distributed via plugin/marketplace (or each repo's `.claude/skills/`) | Skill | Reusable procedure across repos |
| 8 | Project local | `settings.local.json` allow rule | Personal, temporary, gitignored |
| 9 | Organization / managed | Spend limits + OpenTelemetry | Spend controls belong in team setup |
| 10 | Project shared | Permission `ask` rule on edits under `migrations/` (or a `PreToolUse` hook) | Must hold, so enforce it |

</details>
