# Ruby Standards

Preserve the Ruby version/implementation, Bundler lockfile, framework, and existing lint/test conventions; do not assume every Ruby project uses Rails.

- Distinguish `nil` and `false`: `||`/`||=` defaults replace both, and only these two values are falsy. Check string/symbol key contracts at serialization boundaries.
- Avoid accidental mutation through shared arrays/hashes, mutable constants, and shallow copies; keep request/job state out of shared class variables.
- Rescue specific expected errors; bare `rescue` catches `StandardError`, while `Exception` also captures process/control exceptions. Preserve causes and release resources with `ensure`.
- Do not treat the interpreter lock as data-race protection. Understand the chosen runtime, worker/thread model, connection pool, and job retry/idempotency behavior.
- Bound ORM queries and check lazy loading/N+1 behavior. In Rails, distinguish validations/callbacks from database guarantees; use constraints and intentional transaction boundaries.
- Avoid unsafe deserialization, `eval` on untrusted data, and shell-string interpolation. Validate inputs and use existing parameterization/escaping helpers.
- Test framework autoload/eager-load behavior, async jobs, and the supported database where relevant; load [SQL standards](sql.md) for query/schema changes.
