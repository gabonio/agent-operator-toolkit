# Frontend Standards

Apply repository rules and surrounding conventions first.

## Team defaults for new React/TypeScript work

- Use strict types at public/component/API boundaries; isolate and justify any `any`.
- Keep server access in typed clients and data behavior in hooks/services; avoid hidden fetching/persistence in presentational components.
- Do not expose secrets or trusted authorization logic to the browser.
- Model relevant user-visible states and prevent stale requests overwriting newer state.
- Use bounded backend requests and narrow DTOs; never fetch growing datasets for browser filtering.
- Reuse central tokens and shared components from [frontend composition](../architecture/frontend-composition.md).
- Preserve semantic HTML, keyboard access, visible focus, accessible names/status, contrast, reduced motion, responsive layout, and supported themes; test behavior at hook/component boundaries using repository tools.

Do not impose a new state library, CSS framework, component library, test runner, or folder convention on an established repository without an approved reason.
