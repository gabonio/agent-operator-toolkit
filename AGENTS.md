# agent-operator-toolkit AGENTS

These instructions apply anywhere this toolkit is checked out.

`AGENTS.md` is the canonical instruction source for this repo. If other agent-specific files such as `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, or `.github/copilot-instructions.md` exist, they should point back here instead of containing divergent rules.

## Purpose

This repo stores reusable guardrails for AI-assisted coding. Keep it generic, portable, and safe for reuse across personal projects.

Project-specific requirements, architecture, credentials, and business rules belong in the project that owns them, not here.

## Read Order

Before changing this repo:

1. read [README.md](./README.md)
2. read [CODING.md](./CODING.md)
3. read [WORKFLOWS.md](./WORKFLOWS.md) if the task is procedural or multi-step
4. read the relevant file in [coding-standards](./coding-standards) only if the task needs language-specific guidance
5. read [PERSONAS.md](./PERSONAS.md) only if the user wants a role-specific perspective or deliverable

## Scope

Track changes here only for:

- reusable docs
- general coding and safety guardrails
- lightweight sanity-check script

Do not track:

- project-specific business logic
- copied source from another repo
- secrets or credentials
- machine-specific operational notes
- personal completion-reporting or team-notification workflows unless they are explicitly part of the parent project
- generated reports or scratch outputs

## When Used As A Submodule

- the parent repo owns product requirements and project-specific instructions
- this repo owns general AI coding guardrails only
- if a rule only applies to one project, put it in that project instead of this toolkit
- when a project has common developer commands, prefer adding `.vscode/tasks.json` so build, test, lint, and dev flows are available through clickable editor tasks instead of terminal-only instructions

## Documentation Governance

Use the docs like this:

- [README.md](./README.md): what this toolkit is and how it should be used
- [CODING.md](./CODING.md): shared engineering, security, verification, and AI-usage rules
- [WORKFLOWS.md](./WORKFLOWS.md): repeatable safe workflows
- [coding-standards](./coding-standards): concise language-specific checklists
- [PERSONAS.md](./PERSONAS.md): optional specialist-role reference for prompts and deliverables
- [scripts/check](./scripts/check): lightweight toolkit sanity check

## Documentation Maintenance Rules

When new knowledge is learned well enough to keep:

- add general coding or safety policy to [CODING.md](./CODING.md)
- add repeated multi-step execution patterns to [WORKFLOWS.md](./WORKFLOWS.md)
- add setup or usage changes to [README.md](./README.md)
- add reusable specialist-role prompts or response styles to [PERSONAS.md](./PERSONAS.md)
- keep project-specific rules in the project that owns them

Do not duplicate the same guidance across many repos when it can live once here.
