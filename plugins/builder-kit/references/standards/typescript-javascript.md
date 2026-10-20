# TypeScript / JavaScript Standards

Follow the repository's package manager, lockfile, module system, and supported browser/runtime versions; do not force TypeScript onto JavaScript projects.

- TypeScript types disappear at runtime. Validate untrusted JSON, environment variables, and API inputs before narrowing; prefer `unknown` and guards over unchecked assertions or `any`.
- Preserve ESM/CommonJS and package export boundaries. Check resolution in the actual runtime/build, not only the type checker; keep browser bundles free of server-only modules and secrets.
- Handle promise rejection at its owner; await required work and avoid async callbacks in `forEach`. Bound parallel work and account for cancellation and stale results.
- Distinguish missing, `undefined`, `null`, zero, and empty string; use nullish defaults when falsy values are valid. Avoid mutation of shared arrays/objects through aliases.
- Check numeric range and serialization: large integers can lose precision, `BigInt` is not directly JSON-serializable, and dates need explicit timezone/format contracts.
- In JavaScript, use the repository's JSDoc/checking conventions for public contracts. Add type checks only through approved tooling.
- Test boundary validation, async failures/races, and supported execution targets. For browser UI, also load [frontend standards](frontend.md).
