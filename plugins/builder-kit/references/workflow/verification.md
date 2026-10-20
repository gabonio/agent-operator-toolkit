# Verification

Match evidence to risk and changed behavior.

- Run focused tests/checks while iterating.
- Before PR readiness, run the closest feasible local equivalent of the production build or the stricter repository rule.
- Test changed public boundaries, authorization, request scope, contracts, entry paths, and user-visible states where relevant.
- A successful write call is not proof: read back or reconcile important mutations.
- Distinguish local tests/build, CI, review, deployment, and runtime evidence.
- For substantive work, verify a representative capability-to-entrypoint/rule/test path and the documented run/test commands. Review ownership, dependencies, and readable flow against the approved architecture, not a prescribed number of layers.
- Report exact commands/results and limitations. Never claim checks ran when they did not.

Handoff should point to the changed capability paths, existing developer map/run instructions, key decisions, deferred work, and remaining gaps. Update a concise onboarding section only when useful; do not duplicate existing docs or claim maintainability from tests alone.

When full validation is too expensive or unavailable, run the best safe subset, explain the gap, and identify the next required check.
