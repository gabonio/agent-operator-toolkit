# Integration and Trust Boundaries

- Name the authority for each external read/write; separate cached/planned state from write/execution authority.
- Centralize external access behind typed clients/adapters and route related reads consistently.
- Treat caller input as untrusted; enforce validation and object/action authorization on trusted backends.
- Keep secrets, upstream internals, error bodies, and environment routing behind trusted boundaries.
- Use delegated caller authorization when actions must be attributable to that caller.
- Make local bypasses explicit and visibly non-production.
- For cross-repository contracts, deploy providers first and preserve compatibility through migration.
