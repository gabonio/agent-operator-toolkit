# Builder Kit Profiles

Resolve two independent profiles.

## Communication: computer-wide

Values: `non-technical` or `technical`.

- Read `Builder Kit communication profile: <value>` from the active tool's global instructions: `~/.codex/AGENTS.md` for Codex or `~/.claude/CLAUDE.md` for Claude Code; current prompt/project instructions may override it.
- If absent, default to `non-technical` and state that briefly.
- Never edit global instructions without explicit permission.

For `non-technical`, use ordinary language, explain necessary terms once, lead with impact and a recommendation, and avoid unexplained Git/architecture jargon. For `technical`, retain useful terminology, diagnostics, contracts, and tradeoffs. Both profiles preserve the same safety and approval boundaries.

## Delivery: project-specific

Values: `production` or `prototype`.

- Read it from repository instructions or the current explicit request; otherwise default to `production`.
- Never store it globally or infer `prototype` from urgency or user technical level.
- Require explicit prototype confirmation and record the choice in the specification/plan.

For prototype work, also read [prototype delivery](prototype-delivery.md).
