# Java Standards

Apply repository instructions first and delegate platform-specific behavior to an available owning skill.

## General standards

- Prefer constructor injection and immutable dependency fields.
- Avoid wildcard imports except where the repository explicitly permits static test imports.
- Capitalize abbreviations as words in camel/Pascal case, such as `HttpJsonRpcModule`, not `HTTPJSONRPCModule`.
- Use descriptive domain names and stable DTO/contracts instead of exposing persistence entities.
- Keep validation and business rules in their owning boundary; avoid mapper business logic and duplicate guards.
- Express nullability and absence with the repository's established type-system mechanism; do not mix competing annotation/Optional conventions inside one codebase.
- Use typed domain/business errors, preserve causes, and translate technical failures at the owning boundary without leaking internals to clients.
- Remove backend features only after dependent clients have migrated or been removed.
- Inject time and other environmental dependencies for deterministic tests.
- Guard read-then-write races and use transactions/optimistic concurrency where required.
- Test changed behavior at the lowest useful level and at real integration boundaries.
- Use the repository's established telemetry stack for meaningful counters, timings, and traces; do not introduce a competing observability framework casually.
- Match local formatting/import/test naming; do not modernize legacy style incidentally.

## Optional repository conventions

- API → Manager → Service → Repository layering.
- `final var` for non-reassigned locals; no `final` method parameters.
- Test names `methodName_whenCondition_thenExpectedResult` plus user-focused `@DisplayName`.
- Unit tests in the feature module and IoC-backed integration tests in the testing module.
- Injected `Clock` implementations for deterministic time behavior.
- Idempotent persistence callbacks capture only values safe for the storage boundary.

These are examples, not defaults. Confirm them against the current repository before applying them. Error-response conventions, layering, and framework versions are especially repository-specific.
