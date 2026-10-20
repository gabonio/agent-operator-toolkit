# Swift Standards

Respect the package/application target, Swift language mode, minimum OS versions, and existing Apple-platform or server framework.

- Model absence with optionals; avoid forced unwraps/casts for external input. Decode and validate boundary data explicitly.
- Respect actor isolation and `Sendable` contracts; keep UI-owned state on `MainActor`. Do not silence concurrency diagnostics with unchecked annotations without proving safety.
- Give tasks lifecycle ownership and cancellation handling; use detached tasks only with an explicit reason. Cancellation is cooperative and does not undo external side effects.
- Account for actor reentrancy across `await`: state may change before continuation. Recheck invariants before applying stale results.
- Understand ARC ownership and closure capture cycles; use weak captures when ownership requires them, not mechanically. Release observers and other owned resources.
- Distinguish value semantics from shared references inside structs; use correct `String` indices rather than integer byte assumptions. Preserve date, timezone, and numeric serialization contracts.
- Check API availability and exercise the supported OS/runtime, async failures, cancellation, and relevant UI state. A build on the newest SDK alone does not prove minimum-target compatibility.
