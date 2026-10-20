# Ruby Standards

Preserve the Ruby version/implementation, Bundler lockfile, framework, and test conventions; Rails-specific rules apply only when Rails is present.

## Correctness and operations

- Only `nil`/`false` are falsy; `||=` overwrites a meaningful false value. Preserve string/symbol key contracts and avoid aliasing mutable arrays/hashes/constants across requests or jobs.
- Rescue specific expected errors, normally under `StandardError`, not `Exception` (which includes process/control failures). Keep cleanup in `ensure`; a `retry` restarts the protected block, so bound it and account for repeated side effects.
- Make block binding obvious: `render json: records.map do ... end` can bind the block to `render`, not `map`. Parenthesize or split intermediate results; readability here changes behavior, not just style.
- In Rails, bound relations and expose N+1 loading in tests with query assertions or scoped `strict_loading`. Choose `includes`/`preload`/`eager_load` according to query semantics; filtering associated rows can change join behavior.
- Rails bulk methods such as `update_all` bypass model callbacks/validations; enforce invariants in the database and test intentional bypasses.
- External effects generally belong after commit, not `after_save`. An `after_commit` failure cannot roll the database back and can stop subsequent callbacks; use the existing durable delivery/retry design where reliability requires it, rather than assuming callbacks are an atomic queue.
- Respect worker/thread and connection-pool ownership; the interpreter lock is not an invariant lock. Do not interpolate untrusted shell/SQL or deserialize untrusted objects.

## Checks and conventions

- Run the bundled test command and existing `bundle exec rubocop` configuration when installed. Align `TargetRubyVersion` with the oldest supported runtime; distinguish lint/security findings from configurable layout/style preferences.
- For Rails, exercise eager loading/autoloading, jobs, callback failure, and the supported database; use the repository's available `zeitwerk:check` task when applicable.
- Do not impose Rails, a new type checker, frozen-string policy, or a different test framework. Load [SQL standards](sql.md) for query/schema changes.
