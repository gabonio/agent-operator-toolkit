# PHP Standards

Respect the PHP version/extensions, Composer lockfile/autoloading, framework lifecycle, and request versus long-lived worker deployment.

## Correctness and operations

- `declare(strict_types=1)` governs scalar calls from the calling file, not every caller of functions declared there; internal-function calls have exceptions. Validate request values explicitly rather than treating strict types as an input schema.
- Distinguish missing keys from null and valid `"0"` from empty input. Prefer explicit/strict comparisons; avoid numeric-string coercion in identifiers, tokens, or validation.
- PDO placeholders bind whole values, not identifiers, keywords, or an entire `IN` list. Use one placeholder per value and allowlist dynamic identifiers. Reusing a named marker depends on emulation; avoid relying on it for portability.
- Emulated `PDO::prepare()` does not contact the database or validate the statement. Check execution errors and driver/emulation settings; test against the deployed driver/version rather than assuming prepare-time failure.
- In workers, review retained static/singleton state, connections, and memory across jobs; request cleanup assumptions do not automatically hold. Release resources/transactions on failures and distinguish recoverable exceptions from programming errors.
- Escape output for its destination; never deserialize untrusted PHP objects or hide failures with `@`. Verify extension/autoload case sensitivity and runtime restart requirements on the deployment target.

## Checks and conventions

- Run `php -l` on changed files with the target PHP version; it checks syntax, not undefined-function/runtime behavior. Run repository tests and configured Composer scripts.
- Use existing PHPStan/Psalm analysis and project configuration; with PHPStan, adopt explicit rule levels incrementally rather than forcing a moving `max` level or hiding new errors in a widened baseline.
- Keep the declared PSR-12/PER/framework style and formatter. For a new approved style policy, evaluate PHP-FIG PER Coding Style, which supersedes PSR-12, against tool/version support; it is a formatting convention, not a security guarantee. Load [SQL standards](sql.md) for database changes.
