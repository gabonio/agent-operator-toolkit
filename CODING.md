# Shared Coding Standards

These standards are meant to keep AI-assisted changes safe, reviewable, and useful for people who are not full-time developers.

Use them as the default baseline. If a project has stricter local rules, follow the stricter rule.

## Optional Language Guides

Open the relevant guide only when needed:

- [coding-standards/README.md](./coding-standards/README.md)

## Default Operating Rules

- read the existing code before changing it
- make the smallest change that solves the problem
- follow the project's existing patterns before introducing new ones
- keep edits reversible and easy to explain
- state assumptions clearly when requirements are incomplete
- stop and re-check if the requested change has hidden risk or broad blast radius

## Test-First By Default

- when a repo has automated tests, prefer writing the failing test before the implementation for both new behavior and bug fixes
- when a bug is reported, reproduce it with a failing test or the smallest deterministic reproduction before changing the code
- new shared utilities, adapters, and public helpers should not be added untested when the repo has a working test harness
- mock at system boundaries only; avoid mocking the core business logic you are actually trying to verify
- if a repo has no meaningful test setup yet, create the smallest reproducible check you can and say that stronger automated coverage is still missing

## Repository Layout

- durable repo-owned automation belongs under `scripts/`
- keep transient reports, scratch outputs, caches, and generated artifacts out of the repo root unless they are intentionally promoted into maintained assets

## Editor Ergonomics

- when a project has common commands such as build, test, lint, dev, or preview, expose them through `.vscode/tasks.json` when practical
- prefer simple, named tasks over requiring people to remember terminal commands
- mark default build and test tasks using VS Code task groups when the project supports them
- keep tasks thin; they should call stable repo commands or scripts rather than embedding long fragile shell logic
- keep task labels consistent and obvious, such as `build`, `test`, `lint`, `dev`, or `preview`

## Protected Host Paths

These paths are safety spaces. Do not modify them without explicit confirmation for the current task.

Mac paths that require confirmation:

- shell and profile files: `~/.zshrc`, `~/.zprofile`, `~/.zshenv`, `~/.bashrc`, `~/.bash_profile`, `~/.profile`
- SSH and key material: `~/.ssh/`, `~/.gnupg/`
- core OS directories and binaries: `/System/`, `/bin/`, `/sbin/`, `/usr/bin/`, `/usr/sbin/`
- user and global launch config: `~/Library/LaunchAgents/`, `/Library/LaunchAgents/`, `/Library/LaunchDaemons/`
- system and package-manager config: `/etc/`, `/private/etc/`, `/usr/local/etc/`, `/opt/homebrew/etc/`
- system preference and extension locations: `/Library/Preferences/`, `/Library/Extensions/`
- app and cloud credential/config stores: `~/.config/`, `~/Library/Application Support/`

Windows paths that require confirmation:

- shell and profile files: `%USERPROFILE%\\Documents\\PowerShell\\`, `%USERPROFILE%\\Documents\\WindowsPowerShell\\`
- SSH and key material: `%USERPROFILE%\\.ssh\\`, `%USERPROFILE%\\.gnupg\\`
- user and system startup folders: `%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\`, `%ProgramData%\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\`
- core OS and executable locations: `%WINDIR%\\`, `%WINDIR%\\System32\\`, `%ProgramFiles%\\`, `%ProgramFiles(x86)%\\`
- system networking and task scheduling paths: `%WINDIR%\\System32\\drivers\\etc\\`, `%WINDIR%\\Tasks\\`, `%SystemRoot%\\System32\\Tasks\\`
- app and cloud credential/config stores: `%APPDATA%\\`, `%LOCALAPPDATA%\\`, `%USERPROFILE%\\.config\\`

Extra safety rules for these paths:

- prefer additive changes over deletions or rewrites
- for shell/profile files, append or adjust narrowly; do not remove existing lines unless the user explicitly asks for that exact removal
- do not bulk-edit or clean up these paths as a side effect of another task
- do not use destructive commands in these paths unless the user confirms the exact target and intent

## Engineering Principles

- **DRY**: avoid copy-pasted logic
- **KISS**: prefer straightforward solutions over clever ones
- **YAGNI**: do not build for hypothetical future requirements
- **SOLID**: keep responsibilities narrow and boundaries clear
- choose readability over novelty

## Code Quality And Review Hygiene

- use names that explain intent
- keep functions and modules focused
- prefer explicit inputs and outputs over hidden global state
- do not duplicate shared helpers across files; centralize them in one well-named module and reuse them
- keep external IO boundaries explicit: network calls, persistence, and parsing glue should live in dedicated helpers or adapters rather than being scattered inline
- use comments sparingly and only for non-obvious context
- use the project's formatter, linter, type checker, and test runner when available
- keep commits and pull requests focused on one change at a time

## Secure Implementation

Always build secure by default.

### 1. Clarify first

Before implementing:

- identify the user-visible goal
- identify inputs, outputs, and trust boundaries
- note the biggest ways the change could fail or be abused
- prefer standard libraries and well-maintained dependencies

### 2. Implement defensively

- validate inputs using strict schemas or allow-lists where possible
- use safe file and path handling
- validate user-supplied paths against an allowed base directory before reading from disk or passing them to subprocesses
- avoid injection risks in shell commands, SQL, templates, and HTML
- escape or sanitize untrusted content before injecting it into HTML or templates
- do not log secrets, tokens, or sensitive personal data
- do not commit live production data snapshots, customer exports, or other sensitive runtime artifacts
- fail safely and avoid leaking internal details in error messages
- keep permissions narrow and defaults conservative

### 3. Verify before declaring success

- add or update tests when behavior changes
- run the smallest useful verification first, then broader checks
- use read-after-write verification for config, data, or external mutations
- if you could not verify something, say that plainly

### 4. Deliver responsibly

When finishing implementation work, include:

- what changed
- what was verified
- any security-sensitive considerations
- residual risks or follow-ups

## AI-Assisted Coding Rules

- treat AI-generated code as untrusted until reviewed and verified
- never paste secrets, private keys, tokens, or confidential documents into prompts
- keep AI tasks narrowly scoped and easy to check
- do not pretend verification happened when it did not
- prefer incremental edits over large blind rewrites
- ask for confirmation before destructive actions or changes with unclear blast radius
- do not upgrade dependencies, schemas, or build systems casually; explain impact and verify afterward

## Secret Handling

- prefer secret-manager-backed resolution or environment variables over hardcoded values
- use placeholders in docs and examples instead of live secrets
- avoid storing personal identifiers in durable docs when a neutral placeholder works
- prefer `~/...` over a full home path in documentation
- normalize machine-specific paths before committing shared notes

## Verification Rules

- a successful command is not the same as a successful outcome
- prefer read-before-write when the blast radius is unclear
- for destructive or high-risk changes, verify the exact target first and read back immediately after mutation
- verify on the same system or interface that the user will rely on

## Documentation Rules For Code Changes

When behavior changes:

- update the relevant project README if usage changed
- update local instructions if a new quirk or maintenance rule was learned
- update [WORKFLOWS.md](./WORKFLOWS.md) if the change revealed a repeatable process
- update `.vscode/tasks.json` when build, test, lint, dev, or preview commands change in a way users are expected to run from VS Code

## Safety Gate

If a request conflicts with basic safety, security, or data-protection practices:

- do not implement the unsafe version
- offer the safest approach that still meets the user's goal
