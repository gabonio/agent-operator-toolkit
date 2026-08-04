# Frontend Composition

Load for styling, design-system, or reusable-component work.

- Keep primitive values, semantic roles, and component tokens in one central source.
- Components consume semantic/component tokens; page styles contain only genuinely local layout, state, or feature overrides.
- Promote repeated visual or interaction behavior to its shared owner instead of patching copies across pages.
- Build reusable primitives/compositions for recurring controls, panels, badges, skeletons, status surfaces, and dialogs.
- Keep shared components domain-neutral. Pass feature data, persistence, and policy through explicit props/composition.
- Extract a shared contract after repetition is real; do not generalize coincidental markup.
- Include accessibility, focus, responsive behavior, interaction states, reduced motion, and theme behavior in the shared contract.
- Test shared primitives directly and render/inspect representative feature composition in meaningful states/themes.

Preserve the repository's existing design system and tokens; do not copy another application's palette or component names.
