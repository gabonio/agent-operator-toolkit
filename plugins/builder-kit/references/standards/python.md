# Python Standards

Apply repository tooling first.

- Use existing format/lint/type tools; for a new project without them, prefer Ruff unless platform standards say otherwise.
- Separate interfaces/drivers from importable core logic and keep configuration/dependencies explicit.
- Keep UI/CLI state, persistence, logging, and progress at boundaries.
- Type public boundaries, preserve exception causes, and present safe errors at the owner.
- Test core logic without live services and adapters with fixtures/fakes.
- Use the repository entry point or `python -m <module>` for repeatable execution.
- Do not introduce a second formatter, package manager, CLI framework, or project layout without an approved need.
