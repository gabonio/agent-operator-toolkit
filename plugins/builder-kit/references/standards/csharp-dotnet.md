# C# / .NET Standards

Honor the target framework, SDK pinning, nullable context, package management, and established application framework.

- Treat nullable reference annotations as compile-time assistance, not runtime validation. Avoid null-forgiving assertions that hide invalid external inputs.
- Keep asynchronous request paths async end-to-end; avoid `.Result`/`.Wait()` and `async void` except required event handlers. Propagate `CancellationToken` and await work whose failure matters.
- Match dependency-injection lifetimes; never capture a scoped service such as `DbContext` in a singleton or use one context concurrently.
- Dispose owned resources with `using`/`await using`; follow configured HTTP client lifetimes instead of creating clients per request.
- Know when LINQ executes and where: `IQueryable` may translate to SQL, enumeration can repeat queries, and early materialization can pull unbounded data into memory.
- Preserve exception stack traces with `throw;`; translate failures at the owning boundary without leaking details. Make culture, timezone, decimal precision, and serialization contracts explicit.
- Exercise async cancellation, disposal, and real provider translation where relevant; an in-memory database is not proof of relational behavior. Load [SQL standards](sql.md) for query/schema changes.
