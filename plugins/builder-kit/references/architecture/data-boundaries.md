# Sustainable Data Boundaries

Explain unfamiliar database/API terms before asking the user to choose.

Before implementation, answer:

- current/future volume and applicable tenant/time/project/game/team scope;
- pagination/limits and exact fields/DTO;
- where filtering/aggregation executes;
- query/index, payload, and N+1 risk;
- cache bounds, keys/invalidation, staleness, and failure behavior;
- tests proving request scope.

Filter close to the authoritative source. Do not load a whole database, table, or history into server memory or the browser merely to discard most of it. Transfer only needed fields. Keep authorization and object-level filtering on the trusted backend. Client filtering is acceptable only inside an already bounded result.

Prototype exceptions are limited to synthetic or explicitly small bounded data and require a documented ceiling and replacement trigger.

## Database management guardrails

- Add forward migrations with the repository tool; never rewrite an applied migration.
- Enforce durable invariants in the database and validate at application boundaries.
- Use least-privilege identities and approved secret storage; never commit or log credentials.
- Make multi-step writes transactional and plan recovery for risky, volume-sensitive migrations.
- Derive indexes from real queries and validate query plans.
- Define production data ownership, retention/deletion, restore, and capacity monitoring.
