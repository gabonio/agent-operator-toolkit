# Standards Provenance

Maintainer-only source record; runtime workflows must not load it.

Runtime guidance must justify its context cost: keep domain facts, proven friction preventers, and critical safety/authorization boundaries; consolidate duplicates and leave ordinary judgment to the agent.

Sources, curated through 2026-08-04:

- explicit team documentation gathered for the original Builder Kit work;
- accepted-practice analysis from server and tooling changes;
- frontend/backend instructions, architecture, tests, and delivery behavior of real internal tools;
- platform-owned skills as the maintained owner of platform-specific knowledge;
- repository-local instructions and code as the highest practical source for each task.

Refresh standards after material platform/team changes, updating this record with the owning pack. Do not mine PR history on every invocation.

## Public language research

Research date: 2026-10-20. The nine language guides below were revised after visiting the linked public primary sources. Notes identify the rules transferred into each runtime guide; they are a selective synthesis, not copied standards or a claim that all leading teams agree. Language/runtime semantics and documented operational hazards carry different authority from configurable formatting, library API conventions, or framework-specific examples.

Keep these source records out of runtime loading. Recheck version-sensitive advice against the target's pinned tools, database, and framework. No private material, employer-specific policies, installations, or verified hosting compatibility claims are introduced.

### typescript-javascript

- [TSConfig strict](https://www.typescriptlang.org/tsconfig/strict.html), [indexed access](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html), and [exact optional properties](https://www.typescriptlang.org/tsconfig/exactOptionalPropertyTypes.html): compiler-assisted checking of missing values and optional-write contracts; stricter adoption is a configuration decision, not a silent brownfield migration.
- [Typed ESLint promise rule](https://typescript-eslint.io/rules/no-floating-promises/): floating promises, typed-lint cost, and the important exception that `void` suppresses a diagnostic without handling runtime rejection.
- [Node event-loop guidance](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop): small request callbacks, bounded hostile inputs, and the distinction between async APIs and synchronous CPU work. Server guidance is not a blanket ban on synchronous CLI/startup work.
- [Public engineering TypeScript guide](https://google.github.io/styleguide/tsguide.html): minimizing exports, named exports, and type-only import/export conventions. Its introduction explicitly limits applicability outside its original environment; only transferable public guidance is used here. Do not import its toolchain-specific bans or override framework-required exports.

### go

- [Code Review Comments](https://go.dev/wiki/CodeReviewComments): `gofmt`, explicit contexts, consumer-owned interfaces, nil/empty JSON differences, exported contracts, and goroutine lifetimes. This is a review-comment collection, not a complete normative standard.
- [Error wrapping design](https://go.dev/blog/go1.13-errors): `%w` and `errors.Is`/`errors.As`; wrapping exposes implementation details as an API commitment, so translating a storage error can be correct.
- [Database querying](https://go.dev/doc/database/querying): close rows, handle scan errors, check `Rows.Err`, and account for driver placeholders and deferred `QueryRow` errors.
- [Race detector](https://go.dev/doc/articles/race_detector): executable `-race` checks and their executed-path limitation; a clean result cannot establish absence of races in untested paths.

### csharp-dotnet

- [Coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions): configured analysis/editor settings and readable async code. The source distinguishes documentation/samples from runtime/compiler constraints; its newest-language preferences are not imposed on production targets.
- [CA2016](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2016): forwarding cancellation, supported invocation patterns, and intentional non-forwarding exceptions.
- [CA2007](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2007): library versus application `ConfigureAwait` behavior; UI continuations and ASP.NET Core are explicit exceptions to mechanical fixes.
- [CA1851](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1851): repeated deferred enumeration, side effects, and the allocation cost of materialization.
- [EF Core context lifetime](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/): unit-of-work scope, non-thread-safety, immediate awaiting, disposal, unrecoverable context errors, and limitations of an in-memory provider. These rules do not require EF Core in projects using another persistence approach.

### sql

- [PostgreSQL subqueries](https://www.postgresql.org/docs/current/functions-subquery.html): `NOT IN` null semantics, correlated `EXISTS`, and side effects in subqueries. Anti-join choice must preserve intended null semantics.
- [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html): statement snapshots at Read Committed, serialization anomalies/retries, and non-rollback sequence effects. Isolation names/guarantees are engine-specific.
- [CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html): concurrent-build transaction restrictions, invalid-index recovery, and why `IF NOT EXISTS` does not validate the definition.
- [EXPLAIN reference](https://www.postgresql.org/docs/current/sql-explain.html) and [plan interpretation](https://www.postgresql.org/docs/current/using-explain.html): execution/side effects with `ANALYZE`, estimated versus actual cardinality, I/O, and legitimate sequential scans.
- PostgreSQL is the researched concrete engine, not a recommended universal database. Other engines need their own verified syntax, locking, migration, and isolation behavior; SQL capitalization/layout remain local style.

### rust

- [Rust API Guidelines checklist](https://rust-lang.github.io/api-guidelines/checklist.html): newtypes, conversion naming/traits, public examples, and documented error/panic/safety contracts. Library interoperability advice does not mandate new dependencies or every possible trait implementation.
- [Clippy usage](https://doc.rust-lang.org/clippy/usage.html) and [lint categories](https://doc.rust-lang.org/clippy/lints.html): distinguish correctness from opinionated style/pedantic diagnostics, narrowly justified allowances, and the warning against enabling the entire restriction group. Warning-policy commands change across Cargo versions; retain the pinned policy.
- [Cargo test reference](https://doc.rust-lang.org/cargo/commands/cargo-test.html): unit/integration/doctest coverage and target/feature selection; do not assume one maximal feature build proves every supported combination.
- [Async shared-state tutorial](https://tokio.rs/tokio/tutorial/shared-state): short low-contention synchronous critical sections versus locks across suspension. Transfer the ownership/locking reasoning only when async is relevant; do not install its runtime/dependencies or copy its illustrative `unwrap`s. Historical compiler limitations in examples must be rechecked against the actual toolchain.

### kotlin

- [Official coding conventions](https://kotlinlang.org/docs/coding-conventions.html): cohesive related declarations, naming, and the concrete duplicate-JVM-facade hazard in multiplatform filenames. Layout/naming defaults remain subordinate to local conventions.
- [Coroutine cancellation](https://kotlinlang.org/docs/coroutines-cancellation.html): cancellation propagation, cooperative CPU work, interruptible JVM calls, resources lost at suspension boundaries, and bounded non-cancellable cleanup.
- [Android coroutine practices](https://developer.android.com/kotlin/coroutines/coroutines-best-practices): main-safe work, injected dispatchers/scopes, read-only state, shared test schedulers, and `runTest`. Apply lifecycle/ViewModel assumptions only to Android; the guide does not require Android architecture for server or multiplatform projects.

### swift

- [API Design Guidelines](https://www.swift.org/documentation/api-design-guidelines/): evaluate clarity at call sites, argument labels, and names that distinguish mutations from returned values. These are API conventions, not a prescribed formatter.
- [Data-race checking migration guide](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/enabledataracesafety/), read through its [official DocC payload](https://www.swift.org/migration/data/documentation/swift-6-concurrency-migration-guide/enabledataracesafety.json): Swift language mode versus toolchain, Swift 6 checking, Swift 5 assessment flags, and Xcode settings.
- [Language guide concurrency chapter source](https://raw.githubusercontent.com/swiftlang/swift-book/main/TSPL.docc/LanguageGuide/Concurrency.md): structured versus unstructured tasks, inheritance differences, cooperative cancellation, concurrent cancellation handlers, and isolation/suspension reasoning. The rendered migration page required JavaScript, so official payload/source text was used; draft comments in the book source were not treated as shipped features. Check version-dependent isolation defaults rather than assuming `Task {}` moves work off the main actor.

### php

- [Type declarations](https://www.php.net/manual/en/language.types.declarations.php): call-site scalar strictness and internal-call exceptions; strict typing is not input-schema validation.
- [PDO prepare](https://www.php.net/manual/en/pdo.prepare.php): whole-value placeholder limits, duplicate marker/emulation behavior, driver differences, and deferred validation with emulated prepares. Used the maintained reference, not user-contributed comments.
- [CLI options](https://www.php.net/manual/en/features.commandline.options.php): `php -l` syntax-only scope and version-dependent multi-file support.
- [PHP-FIG PSR-12](https://www.php-fig.org/psr/psr-12/) and [PER Coding Style](https://www.php-fig.org/per/coding-style/): the latter supersedes the former and accounts for newer syntax; existing declared framework/formatter policy still wins. Formatting adherence is not evidence of runtime security.
- [PHPStan rule levels](https://phpstan.org/user-guide/rule-levels): incremental checking and the upgrade cost of a moving maximum; not a requirement to install PHPStan or replace Psalm.

### ruby

- [Ruby exception syntax](https://docs.ruby-lang.org/en/master/syntax/exceptions_rdoc.html): default `StandardError`, specific rescue, `ensure`, and protected-block restart with `retry`.
- [RuboCop configuration](https://docs.rubocop.org/rubocop/latest/configuration.html) and [lint reference](https://docs.rubocop.org/rubocop/latest/cops_lint.html): target-version alignment, configurable style versus lint, and ambiguous block association. The tool's defaults are not a universal team standard.
- [Active Record querying](https://guides.rubyonrails.org/active_record_querying.html#eager-loading-associations): query bounds, loading strategy/join semantics, and scoped `strict_loading` for N+1 detection.
- [Active Record callbacks](https://guides.rubyonrails.org/active_record_callbacks.html#transaction-callbacks): bulk-method bypasses, external effects after commit, and the fact that callback exceptions neither roll back committed data nor allow all later callbacks to run. The need for durable delivery where required is an engineering consequence, not a claim that callbacks provide it.

## Research limits

This is a selective primary-source review, not a survey proving what every "world-class" team uses, nor execution of all listed language tools. Public pages and latest/master documentation can change; use the project's actual version and verify details before adoption. Some initially requested documentation paths redirected or were unavailable; only successfully read sources that informed the guides are recorded above. Hosting support/pricing was not researched and remains subject to the stack interview's evidence/approval rules. Contract checks validate instruction packaging and coverage, not deterministic agent behavior or resulting code quality.
