# Data Engineering Lens

- Who owns the datum, and what are its quality/freshness semantics?
- What are current volume, growth, retention, and access patterns?
- What query scope, indexes, partitions, pagination, and payload bounds are required?
- How are schema evolution, backfill, lineage, deduplication, and late/out-of-order data handled?
- Which calculations belong at the source, service, analytical store, or client?
- What cache/materialization bounds and invalidation rules apply?
- How will tests prove scope, correctness, performance assumptions, and migration safety?

Never assume test-sized data represents production growth.
