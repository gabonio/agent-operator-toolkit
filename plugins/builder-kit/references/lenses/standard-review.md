# Standard Review Lens

Review read-only unless changes are separately authorized.

- Establish the approved specification/intent, repository rules, and exact diff/artifact boundary.
- For code, queries, or pipelines, use [standards routing](../standards/routing.md); load only guides matching the changed boundary.
- Check correctness, regressions, contracts/states, triggered security/privacy concerns, maintainability, and evidence.
- Inspect comprehensible domain names, explicit control/data flow, cohesive rule ownership, module dependencies, and abstractions proportional to the change. Preserve brownfield conventions; do not equate domain-driven design with more layers.
- Trace a representative entrypoint to its rule/adapter/test and check the relevant developer map/run instructions. Report concrete navigation or handoff gaps rather than asserting "team-quality" code.
- Verify findings against code or authoritative documentation; distinguish defects from questions.
- Rank actionable findings by severity and location. Avoid unrelated refactors, speculative preferences, and local-style bikeshedding.
- Do not conflate focused tests, build, CI, review, deployment, and runtime checks.
- If there are no findings, say so and name residual evidence gaps.

Standard review asks whether the artifact correctly implements the approved design. When the user wants the design and assumptions challenged, use `$adversarial-review` instead.
