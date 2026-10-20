# Backend Engineering Lens

- What owns the behavior/source of truth, and what contract exposes it?
- Where are validation, authentication, object authorization, and safe error translation enforced?
- Are data scope/payloads bounded, and what consistency, concurrency, retry, or reconciliation is required?
- How are upstream failures, secrets, and environment routing isolated, and which boundary tests prove this?

Prefer cohesive services and root-cause fixes over flags, duplicated validation, or leaky persistence/upstream details.
