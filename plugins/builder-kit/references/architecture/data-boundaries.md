# Sustainable Data Boundaries

Before implementation, answer:

- current and plausible future cardinality;
- time/tenant/project/game/team scope;
- pagination, cursor, window, limit, or justified maximum;
- exact fields transferred and purpose-specific DTO/view contract;
- where filtering, aggregation, and business rules execute;
- indexes/query plan and N+1/payload risks;
- cache bounds, keys, invalidation, and stale behavior;
- partial/failure behavior and request-scope tests.

Filter close to the authoritative source. Do not load a whole database, table, or history into server memory or the browser merely to discard most of it. Transfer only needed fields. Keep authorization and object-level filtering on the trusted backend. Client filtering is acceptable only inside an already bounded result.

Prototype exceptions are limited to synthetic or explicitly small bounded data and require a documented ceiling and replacement trigger.
