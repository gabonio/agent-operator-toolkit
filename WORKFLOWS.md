# Proven Workflows

This file stores repeatable workflows for safe AI-assisted coding. Keep it at the recipe level.

- repeated multi-step flows belong here
- project-specific quirks belong in the project that owns them
- language-specific implementation detail belongs in the relevant coding-standards doc

## 1. First Contact With A Repo

Use this when you are new to a codebase or when an AI assistant is about to make its first change.

### Safe sequence

1. read the repo README and local instructions first
2. inspect the file tree and identify the likely area of change
3. run `git status` before editing anything
4. find an existing example of the same pattern before inventing a new one
5. run the smallest available verification command before changing code

### Practical rules

- prefer reading a few relevant files deeply over scanning the whole repo shallowly
- do not rewrite a file until you understand its role
- if the repo already has conventions, follow them

## 2. Small Bug Fix Workflow

Use this when the goal is to correct existing behavior without redesigning the system.

### Safe sequence

1. identify the expected behavior
2. reproduce the current incorrect behavior if possible
3. locate the smallest responsible area in the code
4. add a failing focused test first when the repo supports testing
5. make the smallest fix that addresses the root cause
6. verify the changed behavior directly

### Practical rules

- fix the cause, not only the symptom
- avoid unrelated cleanup in the same change
- if you cannot reproduce the bug, say so and verify with the best available proxy

## 3. Small Feature Workflow

Use this when the request adds behavior rather than correcting an obvious bug.

### Safe sequence

1. restate the user-visible outcome in one sentence
2. identify acceptance criteria and edge cases
3. find similar code or UI already in the repo
4. add or update focused tests before or alongside the implementation when the repo supports testing
5. implement using existing patterns where possible
6. verify the main path and one failure or edge case
7. update docs or examples if the feature changes usage

### Practical rules

- prefer incremental additions over broad rewrites
- reuse existing types, components, and helper functions before introducing new abstractions
- if the feature needs a bigger design change, pause and surface the tradeoff first

## 4. Config Or Automation Change Workflow

Use this for scripts, local tooling, environment files, automation, or operational config.

### Safe sequence

1. inspect the current config before mutating it
2. identify the narrowest editable target
3. make one scoped change at a time
4. run read-after-write verification
5. record any new maintenance rule or quirk in docs

### Practical rules

- prefer additive changes over replacements
- do not mix config churn with unrelated code changes
- confirm before touching sensitive host paths or credentials

## 5. Dependency Or Toolchain Change Workflow

Use this when changing package versions or build tooling.

### Safe sequence

1. inspect the current dependency or tool version
2. read the relevant config or lockfile before editing
3. change one dependency or toolchain step at a time
4. run focused checks first, then broader checks if available
5. document any breaking change, migration step, or follow-up

### Practical rules

- do not batch unrelated upgrades together
- prefer stable versions and documented migration paths
- if verification is partial, say exactly what remains unverified

## 6. Docs-First Workflow For Non-Developers

Use this when the request is vague or the repo is unfamiliar.

### Safe sequence

1. clarify the goal in plain language
2. translate that goal into a narrow code or docs change
3. inspect the smallest relevant slice of the repo
4. choose the safest implementation path
5. verify and summarize in non-jargon language

### Practical rules

- optimize for clarity and reversibility
- prefer simpler implementations that are easier to explain
- do not hide uncertainty; state assumptions plainly

## 7. Using This Repo As A Submodule

Use this when the toolkit is embedded inside another repo.

### Safe sequence

1. keep project-specific instructions in the parent repo
2. keep general AI coding guardrails in this toolkit
3. update this toolkit only when the guidance is truly reusable across projects
4. avoid turning the toolkit into a copy of one project's internal rules

### Practical rules

- the parent repo owns product knowledge
- this toolkit owns reusable process and safety guidance
- if a rule stops being general, move it out of this repo

## 8. VS Code Tasks Workflow

Use this when setting up a new project or when build, test, lint, dev, or preview commands change.

### Safe sequence

1. identify the commands people are expected to run regularly
2. prefer existing package scripts, make targets, or repo scripts over long inline shell commands
3. create or update `.vscode/tasks.json`
4. define at least the main user-facing tasks such as `build`, `test`, `lint`, `dev`, or `preview` when they exist
5. mark default build and test tasks using VS Code task groups when appropriate
6. run the tasks once from VS Code or via the equivalent command to verify they actually work
7. update the README if the project expects people to use those tasks

### Practical rules

- optimize for clickable, discoverable commands instead of terminal memorization
- keep labels short and stable
- keep tasks workspace-relative
- when a task must stay running, mark it clearly as a watch/dev task instead of pretending it is a one-shot build
- use [templates/vscode/tasks.json.example](./templates/vscode/tasks.json.example) as a starting point when a project does not already have a task file
