# Frontend Standards

Apply repository rules and surrounding conventions first.

## Team defaults for new React/TypeScript work

- Use strict, explicit types at public/component/API boundaries; avoid `any` unless isolated and justified.
- Components use `PascalCase`; hooks/utilities use `camelCase`; constants use the repository convention.
- Keep server access in typed clients/facades and data behavior in focused hooks/services; keep presentational components free of hidden fetching and persistence.
- Do not expose secrets or trusted authorization logic to the browser.
- Model loading, ready, empty, partial, stale, error/retry, and permission states deliberately.
- Prevent older requests from overwriting newer state with cancellation, request generations, or equivalent.
- Prefer narrow backend requests and DTOs; do not fetch an entire growing dataset for browser filtering.
- Reuse central tokens and shared components from [frontend composition](../architecture/frontend-composition.md).
- Preserve semantic HTML, keyboard access, visible focus, accessible names/status, contrast, reduced motion, responsive layout, and supported themes.
- Test hooks/state logic and shared components at their boundaries; render and inspect meaningful states. Use the repository's established unit, component, and end-to-end tools.

Do not impose a new state library, CSS framework, component library, test runner, or folder convention on an established repository without an approved reason.
