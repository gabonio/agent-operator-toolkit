# C# / .NET Standards

Honor `global.json`, target frameworks, nullable context, `.editorconfig`, package policy, and the existing application framework.

## Correctness and operations

- Nullable annotations are not runtime validation. Validate deserialized arguments/configuration and avoid using `!` to conceal invalid state.
- Keep I/O async end-to-end; avoid `.Result`/`.Wait()` in request/UI paths and `async void` except required event handlers. Forward `CancellationToken`; deliberate non-cancellable completion needs an explicit reason.
- Apply `ConfigureAwait(false)` according to context: app-independent libraries may need it; UI continuations may need their captured context, while ASP.NET Core has no synchronization context by default. Do not apply CA2007 fixes mechanically.
- With EF Core, treat `DbContext` as a short-lived unit of work, not thread-safe shared state. Await each operation before reuse; parallel work needs separate contexts. Do not keep a scoped context in a singleton or continue using one after an unrecoverable EF `InvalidOperationException`.
- Understand deferred LINQ execution. Re-enumeration can repeat I/O/side effects; materializing can allocate unbounded data. Keep filtering/projection/bounds server-side before intentional materialization, and inspect real provider translation.
- Dispose owned resources with `using`/`await using`; preserve exception stacks with `throw;`. Keep culture, decimal precision, and time/serialization contracts explicit.

## Checks and conventions

- Run the pinned SDK's build/tests and configured analyzers; use `dotnet format --verify-no-changes` when supported by the repository workflow.
- Inspect CA2016 for token forwarding and CA1851 for repeated enumeration when available. Analyzer availability/default severity varies with the SDK; configure adoption, not blanket suppressions or repository-wide warning escalation.
- Preserve `.editorconfig` naming/formatting. Sample-code conventions are not universal production architecture. Exercise cancellation/disposal and relational behavior against the supported provider; an in-memory fake is not proof. Load [SQL standards](sql.md) for database changes.
