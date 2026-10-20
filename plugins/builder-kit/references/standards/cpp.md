# C++ Standards

Apply repository instructions and local style first.

## Shared standards

- Keep ownership/lifetime explicit. Prefer RAII and existing smart-pointer/result types; never claim ownership of a borrowed raw pointer.
- Follow local value/reference/move conventions and use references for guaranteed dependencies.
- Avoid file/global `using namespace`; respect unity-build constraints on translation-unit internals.
- Preserve the established string, assertion, formatting, and logging types at subsystem boundaries.
- Keep comments for rationale or constraints, not narration.
- Run configured `clang-format` and `clang-tidy`; configure them for new projects unless the toolchain supplies an equivalent.

## Observed practices and conventions

- Use surrounding `C`/`I`/`J`/`S` type prefixes, `E` enum prefix, member style (`m_` or legacy `mName`), and external wire names.
- Common current style: PascalCase methods, camelCase locals, screaming-snake constants, tabs, Allman braces, type-bound pointers/references, and ~120-character lines.
- Follow local include order and `#pragma once`; use established formatting/logging and GoogleTest naming.

Assert macros, constant naming, test naming, and project-namespace versus `std::` string choices vary across codebases. Match the surrounding API and never create a stylistic seam during a legacy fix.
