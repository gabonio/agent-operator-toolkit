# Java Standards

Apply repository instructions first and delegate platform-specific behavior to the owning skills.

## Shared standards

- Prefer constructor injection, immutable dependencies, stable DTO/contracts, and domain names over exposed persistence entities.
- Keep validation/business rules in their owning boundary; preserve causes and translate errors there without leaking internals.
- Follow the repository's nullability/absence mechanism; do not introduce a competing convention.
- Preserve clients before removing backend behavior; guard races and transactional writes where needed.
- Inject time/environment dependencies for deterministic tests and verify real integration boundaries.
- Use existing telemetry, formatting, and static-analysis tools. Ask the backend maintainers before introducing a missing formatter/linter.

## Observed practices and conventions

- Common patterns: layered API → Service → Repository, feature modules, records for DTO/config, `final var` locals, and no `final` parameters.
- Tests commonly use `methodName_whenCondition_thenExpectedResult`, user-focused `@DisplayName`, and unit tests per feature module plus integration tests against real boundaries.
- Inject `InstantSource`/`Clock` for time; keep atomic-update callbacks serializable and idempotent.

Confirm observed practices against the current repository; match local formatting/import style and framework/error conventions.
