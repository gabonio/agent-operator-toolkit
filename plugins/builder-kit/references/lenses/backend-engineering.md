# Backend Engineering Lens

- What service/module owns the behavior and source of truth?
- What is the stable request/response or event contract?
- Where are validation, authentication, object authorization, and error translation enforced?
- Are queries bounded and payloads purpose-specific?
- What transaction, concurrency, idempotency, retry, and reconciliation behavior is required?
- How are upstream failures, timeouts, secrets, and environment routing isolated?
- Which unit, contract, integration, and negative-path tests prove the boundary?

Prefer cohesive services and root-cause fixes over flags, duplicated validation, or leaky persistence/upstream details.
