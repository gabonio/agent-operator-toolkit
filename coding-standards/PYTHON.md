# Generic Python Guardrails

Use this for Python scripts, CLIs, automation, and services.

## Structure

- keep core logic importable and separate from CLI or entrypoint code
- prefer small functions with explicit inputs and outputs
- use `pathlib` for path handling where practical
- use type hints when they improve clarity
- route external HTTP, file persistence, and other side-effectful boundaries through dedicated client or store helpers instead of scattering them across business logic

## Safety

- avoid shelling out when the standard library can do the job safely
- validate untrusted input before using it
- do not hide configuration in module-level globals if it can be passed as parameters
- keep secrets out of code and logs

## Maintainability

- prefer the standard library unless a dependency clearly earns its cost
- use clear names instead of comment-heavy code
- keep side effects near the edges of the program
- avoid broad `except Exception` unless you re-raise or add context deliberately
- do not duplicate shared parsing, normalization, or CLI setup logic across scripts when one shared module can own it

## Verification

- add or update focused tests when behavior changes
- run the repo's formatter, linter, type checker, and tests when available
- verify file writes and external mutations with a read-after-write check
