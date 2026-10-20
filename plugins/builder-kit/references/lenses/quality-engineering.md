# Quality Engineering Lens

- Map acceptance criteria to observable tests at the cheapest reliable level.
- Cover relevant boundaries, negative paths, permissions, concurrency, failure states, and regression seams.
- Prefer characterization tests before changing unclear legacy behavior.
- Mock external systems at boundaries, not internal logic; use deterministic fixtures.
- Verify the real entry path/contract and distinguish focused tests from build, CI, review, deployment, and runtime evidence.
- Identify residual risks automated tests cannot establish.

Avoid brittle implementation-detail assertions and exhaustive low-value permutations.
