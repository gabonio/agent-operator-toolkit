# Swift Standards

Respect `Package.swift`/Xcode targets, Swift language mode (not just compiler version), concurrency settings, minimum OS versions, and the existing framework.

## Correctness and operations

- Validate decoded inputs and model absence with optionals; forced unwraps/casts require a proven invariant, not trust in a server payload.
- Isolate UI state on `MainActor` and honor actor/`Sendable` boundaries. Do not silence diagnostics with `@unchecked Sendable` or unsafe isolation escapes without a documented synchronization proof.
- Recheck state across `await`: actor isolation serializes access but does not make a multi-suspension operation atomic. Keep invariant-changing steps synchronous where possible.
- Prefer structured child tasks for bounded work; both `Task {}` and `Task.detached` are unstructured and need lifetime ownership. Detached tasks do not inherit actor isolation/task-local state; `Task {}` is not a reliable way to move CPU work off the main actor.
- Cancellation is cooperative: use `Task.checkCancellation()` or an explicit cancellation result contract, release resources, and test late results/partial effects. Cancellation handlers can run concurrently with task work.
- Review ARC closure/observer lifetimes; use weak captures according to ownership, not reflexively. Value types may still contain shared references; use proper `String` indices and explicit serialization contracts.

## Checks and conventions

- Run the package's `swift test` or the app's configured Xcode test/build path on supported targets. Check minimum-OS availability, not only the newest SDK.
- Swift 6 language mode enables complete data-race checks. For an approved Swift 5 migration assessment on supported tools, `swift build -Xswiftc -strict-concurrency=complete` (or Xcode Complete checking) surfaces warnings without silently switching language modes.
- Follow API Design Guidelines at the call site: meaningful argument labels and clear mutating/nonmutating pairs such as `sort`/`sorted`. Formatting/linter choices remain repository policy; compiler checks do not prove business invariants or leak freedom.
