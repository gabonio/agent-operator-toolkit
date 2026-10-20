# TypeScript / JavaScript Standards

Respect the package manager/lockfile, compiler configuration, module system, and supported browser/runtime versions. Do not convert JavaScript projects merely to apply this guide.

## Correctness and operations

- Types and assertions do not validate runtime data. Parse external JSON/configuration as `unknown`, validate at entry, and narrow before use; do not hide uncertainty behind `any` or non-null assertions.
- Distinguish missing keys from explicit `undefined`, and absent values from valid `0`, `false`, or `""`. Test dictionary/array misses and partial-update payloads, not just fully populated fixtures.
- Await or return required promises; intentional background work still needs rejection handling and a lifetime owner. `void promise` can satisfy a lint rule but does not catch rejection. Avoid async callbacks to `forEach`; bound concurrent batches.
- On Node request paths, bound JSON/regexp input and CPU work: `async` does not move synchronous work off the event loop. Synchronous startup/short CLI work is a different context.
- Match ESM/CommonJS exports and runtime resolution, using type-only imports where required by the build. Type-checking alone does not prove a package can execute; test the built entrypoint. Keep server-only code/secrets out of browser bundles.
- Define safe-integer, `BigInt` JSON, date/timezone, and serialization contracts at shared boundaries.

## Checks and conventions

- Run the existing typecheck, lint, tests, and target build. For a simple TS project, `tsc --noEmit` checks types; composite/build pipelines may require their configured equivalent.
- For approved new TS configurations, prefer `strict`; assess `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` explicitly rather than assuming `strict` covers them. Stage legacy adoption; retain JavaScript JSDoc/checking conventions.
- When typed ESLint is already available, check `@typescript-eslint/no-floating-promises`; account for its type-information cost and exceptions. Named exports and a small exported surface are useful defaults, not bans on framework-required default exports. Keep repository formatting. For UI, load [frontend standards](frontend.md).
