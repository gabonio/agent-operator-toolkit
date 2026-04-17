# agent-operator-toolkit

`agent-operator-toolkit` is a reusable safety and workflow layer for AI-assisted coding.

It is designed to work either as a standalone repo or as a Git submodule inside personal projects. The goal is simple: give a non-developer using AI a durable set of guardrails for reading code, making small changes safely, verifying work, and keeping project-specific knowledge where it belongs.

## What This Repo Tracks

- shared operator docs:
  - [README.md](./README.md)
  - [AGENTS.md](./AGENTS.md)
  - [CLAUDE.md](./CLAUDE.md)
  - [CODEX.md](./CODEX.md)
  - [GEMINI.md](./GEMINI.md)
  - [CODING.md](./CODING.md)
  - [WORKFLOWS.md](./WORKFLOWS.md)
  - [PERSONAS.md](./PERSONAS.md)
- lightweight language-specific guides:
  - [coding-standards/README.md](./coding-standards/README.md)
- AI compatibility entrypoints:
  - [.github/copilot-instructions.md](./.github/copilot-instructions.md)
- reusable editor templates:
  - [templates/vscode/tasks.json.example](./templates/vscode/tasks.json.example)
- a lightweight sanity check:
  - [`scripts/check`](./scripts/check)

This repo does not replace a project's own source code, README, tests, or architecture docs.

## Instruction Files

`AGENTS.md` is the canonical instruction file for this toolkit.

- Codex uses `AGENTS.md` by default
- Cursor supports `AGENTS.md` directly
- `CLAUDE.md` exists as a compatibility entrypoint and points back to `AGENTS.md`
- `GEMINI.md` exists as a compatibility entrypoint and points back to `AGENTS.md`
- `.github/copilot-instructions.md` exists for GitHub Copilot and points back to `AGENTS.md`
- `CODEX.md` is kept as an explicit compatibility pointer so humans and tools do not invent a second Codex-specific instruction set

The rule is simple: keep the real instructions in one place and make every other agent-specific file defer to it.

## What This Repo Avoids

- business-specific workflows tied to one employer, client, or product
- secrets, credentials, or machine-specific notes
- vendored copies of project code
- large one-off automation scripts that only make sense in a single workspace

## Quick Start

### Use it as a submodule

```sh
git submodule add git@github.com:gabonio/agent-operator-toolkit.git tools/agent-operator-toolkit
```

Then treat the parent project as the source of truth for product requirements and use this toolkit for general coding guardrails.

### Docs-only mode

Use the toolkit without any extra setup:

1. read [README.md](./README.md)
2. read [CODING.md](./CODING.md)
3. read [WORKFLOWS.md](./WORKFLOWS.md)
4. read [AGENTS.md](./AGENTS.md)
5. open [coding-standards/README.md](./coding-standards/README.md) only when you need language-specific guidance
6. open [PERSONAS.md](./PERSONAS.md) only when you want role-specific prompting or outputs

### Sanity check

To verify the toolkit itself is intact:

```sh
./scripts/check
```

## Suggested Layout

One practical setup looks like this:

- your main project repo
- this toolkit as a submodule such as `tools/agent-operator-toolkit`
- local scratch/output folders that stay ignored

## VS Code Preference

This toolkit assumes a VS Code-friendly workflow.

If a project has common commands such as build, test, lint, dev, or preview, prefer exposing them through `.vscode/tasks.json` so they can be run from the editor UI instead of requiring terminal memorization. A reusable starter lives in [templates/vscode/tasks.json.example](./templates/vscode/tasks.json.example).

## Documentation Layout

- [README.md](./README.md): what this toolkit is, how to use it, and where knowledge should live
- [AGENTS.md](./AGENTS.md): canonical cross-agent instruction file
- [CLAUDE.md](./CLAUDE.md), [CODEX.md](./CODEX.md), and [GEMINI.md](./GEMINI.md): compatibility pointers back to `AGENTS.md`
- [.github/copilot-instructions.md](./.github/copilot-instructions.md): GitHub Copilot compatibility pointer back to `AGENTS.md`
- [CODING.md](./CODING.md): shared coding, security, verification, and AI-usage guardrails
- [WORKFLOWS.md](./WORKFLOWS.md): proven generic workflows for safe AI-assisted changes
- [PERSONAS.md](./PERSONAS.md): optional role-based prompting reference
- [coding-standards](./coding-standards): optional language-specific checklists
- [templates/vscode/tasks.json.example](./templates/vscode/tasks.json.example): starter VS Code tasks file for one-click project commands
- [scripts/check](./scripts/check): lightweight toolkit sanity check

## Practical Rule

When new knowledge is learned:

- put reusable coding and safety rules in [CODING.md](./CODING.md)
- put repeatable multi-step workflows in [WORKFLOWS.md](./WORKFLOWS.md)
- put reusable role-based prompting guidance in [PERSONAS.md](./PERSONAS.md)
- put project-specific rules in the project that owns them
- update this README when setup or intended usage changes
