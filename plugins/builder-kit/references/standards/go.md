# Go Standards

Match the module's Go version, dependency policy, and existing formatting/test commands.

- Return and handle errors explicitly; wrap with `%w` when callers need `errors.Is`/`errors.As`. Reserve panics for violated internal invariants, not ordinary input or service failures.
- Pass `context.Context` through request-bound operations; honor deadlines/cancellation and call returned cancel functions. Do not use context as an optional-argument bag.
- Give every goroutine an owner, bounded concurrency, and an exit path. Coordinate shared state; channel closure belongs to the sender/owner, not arbitrary consumers.
- Check typed-nil values stored in interfaces and aliasing of slices/maps. Avoid copying structs containing mutexes.
- Close resources at the correct lifetime, check required write/flush/close errors, and inspect HTTP status codes separately from transport errors.
- Keep interfaces small at consumer boundaries; do not add interfaces or framework layers solely to mock concrete implementation details.
- Use repository checks, `go test`, `go vet`, and the race detector where supported and relevant. Exercise cancellation, goroutine cleanup, and concurrent access, not just happy paths.
