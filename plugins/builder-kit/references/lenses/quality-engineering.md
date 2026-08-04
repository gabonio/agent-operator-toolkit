# Quality Engineering Lens

- Map acceptance criteria to observable tests at the cheapest reliable level.
- Cover boundary values, negative paths, permissions, concurrency, partial/stale/error states, and regression seams.
- Prefer characterization tests before changing unclear legacy behavior.
- Mock external systems at boundaries, not internal logic; use deterministic fixtures.
- Verify the real entry path and contract, not only internal helper output.
- Separate focused iteration evidence from full build, CI, review, deployment, and runtime evidence.
- Identify residual risks that automated tests cannot establish.

Avoid brittle implementation-detail assertions and exhaustive low-value permutations.
