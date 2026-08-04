# Builder Kit Profiles

Resolve two independent profiles after explicit invocation.

## Communication: computer-wide

Values: `non-technical` or `technical`.

- Read `Builder Kit communication profile: <value>` from the active tool's global instructions: `~/.codex/AGENTS.md` for Codex or `~/.claude/CLAUDE.md` for Claude Code.
- A current prompt or project instruction may override it.
- If absent, default to `non-technical`, state the assumption briefly, and offer to save it.
- Never create or edit a global instruction file without explicit permission. Merge one short line; preserve existing content.

For `non-technical`, use ordinary language, explain necessary terms once, lead with impact and a recommendation, and avoid unexplained Git/architecture jargon. For `technical`, retain useful terminology, diagnostics, contracts, and tradeoffs. Both profiles preserve the same safety and approval boundaries.

## Delivery: project-specific

Values: `production` or `prototype`.

- Never read or write this setting globally.
- Read `Builder Kit delivery profile: <value>` from repository instructions when present.
- If absent, default to `production`.
- A current explicit request may override it for the workstream.
- Require explicit confirmation before switching to `prototype`; do not infer it from “quick,” urgency, or user technical level.
- Record the resolved value in the specification and plan.

For prototype work, also read [prototype delivery](prototype-delivery.md).
