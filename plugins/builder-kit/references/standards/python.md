# Python Standards

Apply repository tooling first.

- Follow PEP 8/20 and the existing formatter/linter/type-checker.
- Separate interface/driver concerns from importable core logic.
- Keep core use-case logic stateless where practical; pass configuration as structured inputs rather than reading hidden files/environment inside domain logic.
- Keep UI/CLI state, persistence orchestration, logging, and progress reporting at boundaries.
- Use clear type annotations at public boundaries and structured result/error shapes.
- Avoid broad exception catches; preserve causes and present safe errors at the owning boundary.
- Keep network/filesystem/time dependencies injectable or isolated for testing.
- Unit-test core logic without live services; test adapters at their boundaries using fixtures/fakes.
- Prefer `python -m <module>` or the repository's established entry point for locally repeatable execution.
- Do not introduce a second formatter, package manager, CLI framework, or project layout without an approved need.
