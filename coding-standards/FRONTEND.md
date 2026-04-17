# Generic Frontend Guardrails

Use this for browser UIs and frontend applications.

## Structure

- keep UI components focused on presentation and simple orchestration
- move data fetching, transformations, and reusable logic into dedicated helpers or hooks
- keep network and bridge logic outside the view layer
- prefer existing project patterns before introducing a new state-management approach

## Accessibility And UX

- use semantic HTML where possible
- keep forms labeled and keyboard accessible
- include loading, empty, and error states for async surfaces
- make layouts responsive by default

## Safety

- never embed secrets in client-side code
- validate and sanitize user-provided content before rendering or sending it
- escape untrusted HTML before injecting it into the DOM
- handle errors without leaking internal details

## Maintainability

- keep props and state names explicit
- avoid over-abstracting small UI patterns
- prefer strong typing for component props and API responses
- for drag, resize, scroll, and pointer-heavy interactions, batch or schedule UI updates and avoid full rerenders on every event when a narrower update will do

## Verification

- test the main user flow and one edge case
- run the project's lint, type, and test commands when available
- verify the changed screen on both narrow and wide layouts when relevant
