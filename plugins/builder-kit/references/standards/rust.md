# Rust Standards

Respect the crate's edition, minimum supported Rust version, features, and existing Cargo/clippy/formatting policy.

- Express ownership and borrowing deliberately; do not clone large data or add `Arc<Mutex<_>>` just to silence the compiler.
- Use `Result` and typed errors for recoverable failures, preserving sources. Avoid `unwrap`/`expect` on external input or fallible production paths; justify invariant-based exceptions.
- Keep `unsafe` minimal and document its safety invariants, including aliasing, lifetimes, and FFI ownership. Safe compilation does not establish business correctness.
- In async code, avoid blocking executor threads or holding synchronous locks across `.await`; bound spawned work and account for cancellation/drop cleanup.
- Do not assume a future is cancellation-safe: partial writes and external side effects may survive a dropped future. Design retries around actual operation semantics.
- Check integer overflow/conversions, UTF-8 byte versus character boundaries, and platform-dependent sizes at public/serialization boundaries.
- Exercise relevant feature combinations and targets as well as error/cancellation paths; use repository tests and static checks, with specialized unsafe-code tools only when available and relevant.
