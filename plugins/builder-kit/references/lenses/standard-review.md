# Standard Review Lens

Review read-only unless changes are separately authorized.

- Establish the approved specification/intent, repository rules, and exact diff/artifact boundary.
- Check correctness, regressions, contracts/states, triggered security/privacy concerns, maintainability, and evidence.
- Verify findings against code or authoritative documentation; distinguish defects from questions.
- Rank actionable findings by severity and location. Avoid unrelated refactors, speculative preferences, and local-style bikeshedding.
- Do not conflate focused tests, build, CI, review, deployment, and runtime checks.
- If there are no findings, say so and name residual evidence gaps.

Standard review asks whether the artifact correctly implements the approved design. When the user wants the design and assumptions challenged, use `$adversarial-review` instead.
