# Verification

Match evidence to risk and changed behavior.

- Run focused tests/checks while iterating.
- Before PR readiness, run the closest feasible local equivalent of the production build or the stricter repository rule.
- Test public boundaries, request scope, authorization, environment routing, contracts, and direct entry paths when relevant.
- Exercise loading, ready, empty, partial, stale, error, retry, permission, and prototype/mock states that the feature exposes.
- A successful write call is not proof: read back or reconcile important mutations.
- Distinguish local tests, local build, remote CI, adversarial review, human review, deployment, and runtime verification. One does not prove another.
- Report exact commands/results and limitations. Never claim checks ran when they did not.

When full validation is too expensive or unavailable, run the best safe subset, explain the gap, and identify the next required check.
