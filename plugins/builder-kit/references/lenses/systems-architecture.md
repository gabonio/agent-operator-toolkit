# Systems Architecture Lens

- Define responsibilities/authorities and trace flow across trust/deployment boundaries.
- Identify coupling, failure propagation, and blast radius.
- Prefer the simplest boundary that preserves independent evolution.
- For new capability/ownership boundaries, apply [domain organization](../architecture/domain-organization.md): domain vocabulary, cohesive modules, explicit dependencies, and a traceable entrypoint-to-rule path without mandatory layers or services.
- Specify compatibility, provider-before-consumer migration, rollback, and evidence.
- Challenge duplicate state or new technology without a measured need.

Do not redesign a whole system for a local change. Apply this lens when the boundary or blast radius is genuinely cross-cutting.
