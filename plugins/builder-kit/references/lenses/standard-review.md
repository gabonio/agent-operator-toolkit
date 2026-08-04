# Standard Review Lens

Review read-only unless changes are separately authorized.

- Establish the approved specification/intent, repository rules, and exact diff/artifact boundary.
- Check correctness, regressions, contracts, error/state behavior, security/privacy triggers, maintainability, and test evidence.
- Verify findings against code or authoritative documentation; distinguish confirmed defects from questions.
- Rank actionable findings by severity and location. Avoid unrelated refactors, speculative preferences, and local-style bikeshedding.
- Confirm whether focused tests, production-like build, CI, review, deployment, and runtime checks actually ran; do not conflate them.
- If there are no findings, say so and name residual evidence gaps.

Standard review asks whether the artifact correctly implements the approved design. When the user wants the design and assumptions challenged, use `$adversarial-review` instead.
