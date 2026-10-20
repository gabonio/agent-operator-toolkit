# Kotlin Standards

Identify the target first: JVM/server, Android, or multiplatform. Preserve its Kotlin, build-plugin, runtime, and lifecycle conventions.

- Prefer explicit null handling to `!!`; Java platform types and deserialized inputs can still violate Kotlin null assumptions.
- Use structured coroutines with a lifecycle owner, appropriate dispatcher, and bounded concurrency. Do not block event/UI threads or launch unowned `GlobalScope` work.
- Preserve coroutine cancellation; do not swallow `CancellationException` in broad catches or `runCatching` recovery paths. Account for cleanup and partial side effects.
- Match Flow collection to lifecycle and intended hot/cold semantics; avoid duplicate upstream work, missed updates, and non-atomic shared-state changes.
- A read-only `List` is not necessarily immutable; data-class `copy` is shallow. Protect mutable collections crossing ownership or concurrency boundaries.
- Verify Java interop, serialization defaults, equality, and persistence/framework proxy requirements instead of assuming Kotlin defaults fit every framework.
- Test coroutine scheduling/cancellation and the actual platform boundary. Load [Java standards](java.md) only for relevant JVM interop, and [SQL standards](sql.md) for database changes.
