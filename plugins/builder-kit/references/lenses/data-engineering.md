# Data Engineering Lens

- Who owns the data, and what are its quality/freshness semantics?
- What volume, growth, retention, query scope, pagination, and payload bounds apply?
- How are schema evolution, backfill, lineage, deduplication, and late data handled?
- Where should calculations/cache materialization live, and how will tests prove scope and migration safety?

Never assume test-sized data represents production growth.
