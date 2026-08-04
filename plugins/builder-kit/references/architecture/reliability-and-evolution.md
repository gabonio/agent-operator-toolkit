# Reliability and Evolution

Model relevant states explicitly: initial loading, ready, background refresh, empty, partial, stale, error/retry, permission-limited, and mock/prototype. Preserve useful ready data during localized refresh when safe and prevent stale asynchronous responses from overwriting newer state.

For mutations:

- validate and authorize at boundaries;
- use transactions for multi-step persistence;
- use guarded writes or optimistic concurrency when lost updates are possible;
- make retries/external triggers idempotent where applicable;
- distinguish local-save success from downstream-sync failure;
- read back or reconcile important externally owned writes.

For evolution:

- add forward migrations; never rewrite an applied numbered migration;
- preserve public/client compatibility until consumers migrate;
- keep generated contracts synchronized;
- treat published versions as immutable;
- order providers before consumers;
- define rollout, rollback, and observable success for risky changes.
