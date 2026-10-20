# SQL Standards

Identify the database engine/version and migration tooling first. SQL is a data/query language, not by itself an application runtime or deployment stack.

- Bind values as parameters, never concatenate untrusted input. Dynamic identifiers/sort directions need an allowlist and engine-correct quoting; they are not ordinary value parameters.
- Model `NULL` deliberately: use `IS NULL`, check three-valued logic and `NOT IN` with nullable rows, and distinguish `COUNT(*)` from `COUNT(column)`.
- Specify stable ordering with a unique tie-breaker for pagination; bound result sets. Check join cardinality to prevent duplicates and inflated aggregates.
- Use constraints for invariants; choose transaction boundaries and isolation for races. Retry only known transient failures with a safe, bounded whole-operation policy.
- Inspect representative execution plans, indexes, data volume, and lock behavior. ORM abstractions and tiny fixtures do not prove production query cost.
- Plan compatible migrations/backfills and recovery for the actual engine; DDL transaction support, online index operations, and locking differ. Flag destructive or irreversible changes before execution.
- Choose exact numeric types and timestamp/timezone semantics deliberately. Test constraints, nulls, concurrent writes, ordering, and migrations against the supported engine, not a substitute dialect.
