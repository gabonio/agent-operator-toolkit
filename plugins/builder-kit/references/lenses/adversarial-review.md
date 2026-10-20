# Adversarial Review Lens

Challenge material decisions and readiness, not wording or local style. For each finding give the challenged assumption, plausible failure, evidence versus inference, impact/likelihood, and cheapest useful validation or mitigation.

For implementation readiness, challenge unclear domain ownership, hidden side effects/dependencies, unnecessary abstraction, and an unverified developer handoff. Trace the changed path and tests; do not infer maintainability from folder names or demand an unrelated brownfield redesign.

Default to at most five findings. Classify each as must fix, should fix, accepted risk, or user decision; then report strengths, residual risks, and `ready`, `ready with accepted risks`, `revise`, or `blocked on decision`.

Do not manufacture certainty, duplicate findings, bikeshed established style, or continue when objections have low expected value. A same-context multi-lens pass is not independent review; name the review mechanism honestly. Remain read-only unless changes are separately authorized.
