# PHP Standards

Follow the supported PHP version/extensions, Composer lockfile/autoloading, framework lifecycle, and deployment model.

- Use the project's typing policy; `strict_types` is per-file and does not validate request payloads. Validate external data before domain use.
- Prefer strict comparisons; account for numeric-string coercion and `empty()` treating `"0"` as empty. Distinguish absent keys from keys containing `null`.
- Use parameterized database access and context-appropriate output escaping. Framework helpers are not permission to trust dynamic SQL identifiers, templates, or unserialized user input.
- Respect request versus long-lived worker lifetimes: static/singleton state can leak across jobs or users. Reset scoped state and bound worker resource use.
- Handle `Throwable` at the appropriate boundary without masking programmer errors; release resources and roll back failed transactions. Do not suppress failures with `@`.
- Check installed extensions, autoload/case sensitivity, configuration, and worker/opcache restart requirements in the actual target environment.
- Test through repository tooling, including framework/container boundaries and supported database behavior. Load [SQL standards](sql.md) when queries or schema change.
