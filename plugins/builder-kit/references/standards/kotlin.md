# Kotlin Standards

Identify JVM/server, Android, or multiplatform first. Preserve Kotlin/Gradle plugin versions, source sets, and platform lifecycle.

## Correctness and operations

- Handle platform types and deserialized nulls explicitly rather than using `!!`. Keep Java interop and framework/proxy contracts visible; Kotlin null safety does not sanitize external input.
- `suspend` does not make blocking code main-safe. Move blocking work at its owner to an appropriate dispatcher; inject dispatchers when tests need control instead of scattering hardcoded dispatchers.
- Prefer structured scopes for caller-owned work. Work that intentionally outlives a screen/request needs a longer-lived, explicitly owned scope, not unowned `GlobalScope` launches. Bound fan-out.
- Rethrow `CancellationException` from broad catches or `runCatching` recovery. Cancellation is cooperative: CPU loops need `ensureActive()`/`yield()` as appropriate; moving blocking JVM calls to an I/O dispatcher alone does not make them interruptible.
- Release acquired resources even if cancellation happens before a suspended call returns them. Keep cleanup in `finally`/`use`; use non-cancellable blocks only for necessary bounded cleanup, not whole operations.
- Expose read-only state instead of mutable Flow/collections; read-only views and data-class `copy` do not imply deep immutability. Align collection with lifecycle and hot/cold semantics.
- In multiplatform code, same-package top-level declarations in identically named common/JVM files can produce duplicate JVM facades. Use platform-suffixed filenames where needed.

## Checks and conventions

- Use the Gradle wrapper's actual compile/test tasks for affected source sets; server `test` alone does not validate Android/native targets. Run existing lint/static analysis rather than adding tools implicitly.
- Where `kotlinx-coroutines-test` exists, use `runTest` and test dispatchers sharing one scheduler; test cancellation/cleanup and controlled virtual time, not sleep-based timing.
- Follow the official Kotlin convention as a new-code default, including cohesive top-level declarations rather than forced one-class files; preserve local formatting. Load [Java standards](java.md) for JVM interop or [SQL standards](sql.md) for database changes only.
