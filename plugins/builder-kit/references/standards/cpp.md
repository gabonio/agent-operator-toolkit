# C++ Standards

Apply repository instructions and local style first.

## General standards

- Use descriptive, consistent vocabulary. Types and variables are nouns; functions are command verbs. Do not mix synonyms such as listener/callback/handler for one concept.
- Keep classes cohesive and files focused. Prefer one clear class owner per header/source pair where that is the repository pattern.
- Prefer returning values over output parameters. Put inputs before unavoidable outputs and replace unclear boolean flags with a descriptive `enum class`.
- Prefer RAII, `std::unique_ptr`/`std::make_unique`, and the Rule of Zero; avoid manual `new`/`delete`. Never create an owning smart pointer from a raw pointer owned elsewhere.
- Follow the Rule of Five when a class must own a special member: explicitly implement, default, or delete the remaining copy/move operations as appropriate.
- Use `nullptr`, initialize members at declaration where practical, mark overriding methods with `override` rather than redundant `virtual`, and keep const-correctness. Use `constexpr` for compile-time values.
- Pass small trivially copyable values by value and larger read-only inputs by `const&`. For constructor/factory sink parameters, follow the local move/ownership convention rather than forcing `const&`.
- Use references for guaranteed dependencies and the repository's required-value assertion pattern. Make optional ownership and lifetime explicit.
- Do not add new C strings; use the string/view type already established at the boundary.
- Use `expected`/result/optional patterns for recoverable failure in no-exception code.
- Never use `using namespace` at file/global scope. Keep translation-unit internals in the repository's established namespace form; avoid anonymous namespaces when unity builds can collide.
- Mark intentional non-empty switch fallthrough with `[[fallthrough]]`. Avoid chained assignments and other compact forms that obscure state changes.
- Keep comments for rationale, constraints, and non-obvious behavior; do not restate the code or add artificial separators.

## Optional legacy conventions

- Types use `C`/`I`/`J`/`S` prefixes where the surrounding subsystem does; external wire DTOs keep wire names.
- Prefer `m_` members for new code, but accept `mName` in active legacy areas and never mix styles inside one unit.
- `enum class` with `E` prefix unless enclosing scope already disambiguates.
- Methods/functions use PascalCase command verbs; locals use camelCase; constants use screaming snake case.
- Tabs, Allman braces, braces on all control flow, pointer/reference bound to the type, and approximately 120-character soft lines.
- Use `#pragma once`; group self/project/framework/STL includes following the local order.
- Use `fmt::format` and the established formatted logging macro.
- GoogleTest names use PascalCase behavior descriptions.

These conventions are examples found in some mature C++ codebases, not universal defaults. Apply them only when the repository already uses them. Assertion macros, string types, constant naming, and test naming vary; match the surrounding API and never create a stylistic seam during a legacy fix.
