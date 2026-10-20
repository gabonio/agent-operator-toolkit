# Reliability and Evolution

Model only states the feature exposes: loading/ready, empty/partial/stale, error/retry, permission, and prototype. Preserve usable data during refresh when safe and prevent stale responses overwriting newer state.

For mutations:

- validate and authorize at boundaries;
- use transactions for multi-step persistence;
- use guarded or optimistic concurrency where lost updates are possible;
- make retried mutations/effects idempotent;
- distinguish local success from downstream failure;
- read back or reconcile important externally owned writes.

For evolution:

- add forward migrations; never rewrite an applied migration;
- identify actual consumers and migration paths before choosing compatibility policy;
- preserve compatibility until required consumers migrate; document any bounded-prototype exception;
- do not assume automatic updates make breaking changes safe; verify coordinated rollout timing and fallback behavior;
- keep generated contracts synchronized;
- treat published versions as immutable;
- order providers before consumers and define rollback/observable success for risky changes.
