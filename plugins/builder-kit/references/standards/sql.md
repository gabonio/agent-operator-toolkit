# SQL Standards

Identify the database engine/version, driver, and migration runner first. SQL complements an application stack; PostgreSQL examples below are not portable guarantees.

## Correctness and operations

- Bind values; allowlist dynamic identifiers/sort directions and quote with engine-aware APIs. A value placeholder cannot represent an identifier or an entire `IN` list.
- Test three-valued logic: nullable `NOT IN` can yield unknown rather than true. Prefer a correctly correlated `NOT EXISTS` when that expresses the intended anti-join; define left-side null semantics. Check join multiplicity before aggregating and distinguish `COUNT(*)` from `COUNT(column)`.
- Bound reads and order pages with a unique tie-breaker. Choose exact numeric types and explicit timezone semantics; preserve contracts across drivers.
- Put invariants in constraints, not only application checks. In PostgreSQL Read Committed, successive statements can see different snapshots; a transaction alone does not protect read-then-write decisions. Choose guarded writes, locks, or stronger isolation based on the invariant.
- Retry serialization failures by restarting the whole transaction, with a bound and safe external-effect handling; do not retry arbitrary integrity errors.
- Plan compatible migrations, bounded backfills, lock budgets, and recovery. PostgreSQL `CREATE INDEX CONCURRENTLY` cannot run inside a transaction block and a failed build can leave an invalid index. Inspect validity and resolve the failure; do not assume `IF NOT EXISTS` verifies an index definition.

## Checks and conventions

- Inspect engine-native plans on representative distributions; compare estimated/actual row counts and I/O. A sequential scan is not automatically a defect.
- PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)` executes the statement, including write/function side effects. Use an authorized safe environment; rollback does not undo every possible effect.
- Test nulls, uniqueness, concurrency, and migration/recovery against the supported engine. Use existing dialect-aware lint/migration checks; capitalization, CTE layout, and naming are team conventions, not query-correctness rules.
