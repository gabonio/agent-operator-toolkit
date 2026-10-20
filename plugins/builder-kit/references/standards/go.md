# Go Standards

Match the module's Go version, build tags, dependency policy, and package contracts.

## Correctness and operations

- Return errors, not sentinel success values or panics for ordinary failures. Use `errors.Is`/`errors.As` for wrapped errors. `%w` exposes the cause as part of the public API: translate storage/provider errors when callers should not depend on them.
- Pass `context.Context` first through request-bound calls, honor cancellation, and release timeout resources. Do not stash request contexts in structs or replace them with `Background()` to escape cancellation; interface-required signatures are an exception.
- Give goroutines bounded fan-out, an owner, and an exit/join path, including blocked channel operations. Garbage collection does not stop leaked goroutines. The sending owner closes channels; test cancellation before and during sends.
- Check typed-nil interfaces, slice/map aliasing, and copied mutex-bearing structs. A nil slice and an empty slice encode differently in JSON; preserve the response contract.
- With `database/sql`, close `Rows`, check `Scan` errors and `rows.Err()` after iteration; `QueryRow` reports query failures through `Scan`. Use context-aware calls and driver-appropriate placeholders. Load [SQL standards](sql.md) for query/schema changes.
- Close owned HTTP bodies and check status codes independently of transport errors; keep cleanup scoped so looped defers do not retain growing resources.

## Checks and conventions

- Use `gofmt` and repository tests; run `go vet ./...` and `go test ./...` for the relevant module when feasible. Exercise actual build tags/platforms.
- Run `go test -race` on concurrency-sensitive packages where supported. A clean run covers only executed paths; test goroutine shutdown as well as shared-memory access.
- Define small interfaces where consumers need them, not speculative producer-side interfaces solely for mocking. Keep naming/package layout local; document exported contracts and provide runnable examples for new public APIs.
