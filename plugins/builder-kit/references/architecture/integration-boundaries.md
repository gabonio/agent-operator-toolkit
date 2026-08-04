# Integration and Trust Boundaries

- Name the authoritative owner of every external datum and mutation.
- Separate cached/read models from write authorities and planning state from execution state.
- Treat browsers and caller-controlled input as untrusted.
- Centralize external access behind typed clients, adapters, or facades.
- Keep secrets, upstream internals/error bodies, environment routing, and authorization enforcement behind trusted boundaries.
- Use the caller's delegated authorization when actions must be attributable to that caller.
- Validate inputs and object-level access on the backend; never rely on hidden UI controls.
- Make local bypasses explicit and visibly different from deployed behavior.
- Route related reads consistently so environments/sources cannot be mixed accidentally.
- For cross-repository contracts, deploy the provider before its consumers and preserve compatibility until migration completes.
