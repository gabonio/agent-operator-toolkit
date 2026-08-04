# Authority and legacy guidance

Apply guidance in this order:

1. Safety, security, and explicit user instructions.
2. Resolved communication and delivery profiles for the task.
3. Repository instructions, specifications, ADRs, build files, and contracts.
4. Conventions in the surrounding code.
5. Evidence-backed organization or team standards supplied by the user or repository.
6. Builder Kit defaults.

Label guidance where ambiguity matters: `universal`, `team default`, `repository family`, `observed practice`, `legacy-compatible`, or `unsettled`.

For legacy code, make the smallest coherent change and match local naming, structure, and error handling. Do not modernize unrelated code or create a stylistic seam. When refactoring is the approved objective, define its boundary, compatibility plan, migration, and verification explicitly.

Inspect history only when current documentation and code are missing or contradictory. Treat historical practice as evidence, not automatic authority.
