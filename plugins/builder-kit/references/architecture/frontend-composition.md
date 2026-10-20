# Frontend Composition

Load for styling, design-system, or reusable-component work.

- Keep tokens and shared visual behavior in their central owner; leave only local layout/state overrides on pages.
- Extract shared components after repetition is real, and keep them domain-neutral through props/composition.
- Include accessibility, focus, responsive/theme behavior, reduced motion, and interaction states in the shared contract.
- Test shared primitives and render representative feature states.

Preserve the repository's existing design system and tokens; do not copy another application's palette or component names.

When the repository or platform provides a maintained component library or frontend skill, prefer it and delegate platform specifics to it unless the user or product evidence requires another direction.

Reuse approved assets/fonts and verify licensing before adding new ones.
