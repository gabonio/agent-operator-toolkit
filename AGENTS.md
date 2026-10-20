# Agent Operator Marketplace AGENTS

These instructions apply anywhere this toolkit is checked out.

`AGENTS.md` is the canonical instruction source for this repo. The `CLAUDE.md`, `CODEX.md`, and `GEMINI.md` compatibility files point back here instead of containing divergent rules.

## Purpose

This repo is a portable multi-agent marketplace for reusable AI-development plugins and skills. Keep distribution infrastructure generic, keep each plugin self-contained under `plugins/`, and use native Codex, Claude Code, GitHub Copilot, and Gemini CLI surfaces.

Project-specific requirements, credentials, proprietary systems, employer names, and business rules belong in the project or private plugin that owns them, not here.

## Read Order

Before changing this repo:

1. read [README.md](./README.md)
2. read [WORKFLOWS.md](./WORKFLOWS.md) for plugin or release work
3. read the target plugin's `SKILL.md` and directly referenced guidance

## Scope

Track changes here only for:

- reusable, organization-neutral plugins under `plugins/`
- Codex and shared Claude Code/GitHub Copilot marketplace registries
- Gemini CLI extension metadata, commands, and skill entrypoints
- marketplace contributor documentation
- lightweight validation and release automation

Do not track:

- project-specific business logic
- vendored application or business-logic source unrelated to a marketplace plugin
- secrets or credentials
- machine-specific operational notes
- internal commands, private workflows, or proprietary platform guidance
- generated reports or scratch outputs

## Plugin boundaries

- the target project owns product requirements and project-specific instructions
- each plugin owns only its reusable workflow and references
- marketplace root files own discovery, validation, and publishing behavior
- do not make one plugin depend on an organization-only bot, slash command, or service

## Documentation Governance

Use the docs like this:

- [README.md](./README.md): marketplace usage and structure
- [WORKFLOWS.md](./WORKFLOWS.md): plugin addition and release workflows
- `.claude-plugin/marketplace.json`: shared Claude Code and GitHub Copilot marketplace registry
- `.agents/plugins/marketplace.json`: Codex marketplace registry
- `gemini-extension.json`, `commands/`, and `skills/`: Gemini CLI extension surface
- `plugins/`: installable plugin roots
- [scripts/check](./scripts/check): marketplace validation

## Documentation Maintenance Rules

When new knowledge is learned well enough to keep:

- add general marketplace policy to this file
- add repeated marketplace maintenance patterns to [WORKFLOWS.md](./WORKFLOWS.md)
- add setup or usage changes to [README.md](./README.md)
- keep `README-CODEX.md`, `README-CLAUDE.md`, `README-COPILOT.md`, and `README-GEMINI.md` aligned with native client commands
- keep plugin behavior in the owning plugin
- keep project-specific rules in the project that owns them

Do not duplicate the same guidance across many repos when it can live once here.
