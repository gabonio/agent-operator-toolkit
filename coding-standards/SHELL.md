# Generic Shell Guardrails

Use this for Bash, Zsh, and portable shell automation.

## Structure

- keep scripts short and task-focused
- factor repeated logic into functions
- prefer a maintained script over a long copy-pasted command sequence

## Safety

- use strict mode when practical: `set -euo pipefail`
- quote variable expansions unless you explicitly need word splitting
- use temporary files safely
- avoid destructive commands by default
- validate paths and arguments before mutating files

## Maintainability

- keep environment assumptions explicit
- prefer descriptive variable names over terse one-letter names
- print clear status and error messages
- avoid relying on interactive prompts in automation

## Verification

- run `shellcheck` when available
- test scripts in the smallest safe scope first
- verify that outputs and side effects match the intended target
