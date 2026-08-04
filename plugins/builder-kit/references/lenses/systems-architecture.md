# Systems Architecture Lens

- Define component/service responsibilities and authoritative owners.
- Trace data and control flow across trust and deployment boundaries.
- Identify coupling, availability dependencies, failure propagation, and blast radius.
- Prefer the simplest boundary that preserves independent evolution.
- Specify compatibility, versioning, provider-before-consumer ordering, migration, and rollback.
- Challenge synchronous coupling, duplicate state, and technology additions without a measured need.
- Record the operational evidence needed to validate architectural assumptions.

Do not redesign a whole system for a local change. Apply this lens when the boundary or blast radius is genuinely cross-cutting.
