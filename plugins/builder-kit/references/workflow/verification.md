# Verification

Match evidence to risk and changed behavior.

- Run focused tests/checks while iterating.
- Before PR readiness, run the closest feasible local equivalent of the production build or the stricter repository rule.
- Test changed public boundaries, authorization, request scope, contracts, entry paths, and user-visible states where relevant.
- A successful write call is not proof: read back or reconcile important mutations.
- Distinguish local tests/build, CI, review, deployment, and runtime evidence.
- Report exact commands/results and limitations. Never claim checks ran when they did not.

When full validation is too expensive or unavailable, run the best safe subset, explain the gap, and identify the next required check.
