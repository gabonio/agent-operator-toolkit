# Rust Standards

Respect the crate's edition, minimum supported Rust version (MSRV), targets/features, and pinned Cargo toolchain.

## Correctness and operations

- Model distinct identifiers/units with newtypes where interchange is dangerous. Keep ownership explicit; do not clone large values or introduce shared locking just to satisfy borrowing.
- Return meaningful `Result` errors with sources for recoverable failures. Document public APIs' error, panic, and safety contracts. `unwrap`/`expect` may express a proven invariant or test setup, not validation of external input.
- Use checked conversions for narrowing, consider overflow behavior, and distinguish UTF-8 byte offsets from character boundaries. Public formats must not depend on platform-sized integers accidentally.
- Keep `unsafe` small with explicit aliasing/lifetime/FFI invariants. Compilation does not prove an unsafe abstraction sound or a domain rule correct.
- In async code, release synchronous guards before `.await`; a short low-contention synchronous critical section can be appropriate. Do not replace every mutex with an async mutex. Use the existing runtime's blocking-work facility when needed, not a newly imposed runtime.
- Review cancellation/drop paths for lost partial work and external effects; bound tasks and define who joins or cancels them.

## Checks and conventions

- Run `cargo fmt --check`, repository tests (including doctests for public examples), and `cargo clippy` with the project's targets/features. Check the MSRV, not only the newest compiler; test supported feature combinations instead of blindly enabling mutually exclusive features together.
- Fix Clippy correctness diagnostics; evaluate style/pedantic suggestions in context. Never enable the entire `clippy::restriction` group; select relevant lints and narrowly justify exceptions. Preserve the pinned CI warning policy.
- For library APIs, follow `as_`/`to_`/`into_` conversion naming and standard conversion traits where semantics fit. Do not derive traits with misleading equality/ownership semantics or introduce serialization dependencies merely to satisfy a checklist.
