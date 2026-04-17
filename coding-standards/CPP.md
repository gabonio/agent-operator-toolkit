# Generic C And C++ Guardrails

Use this for small, safe AI-assisted changes in C or C++ codebases.

## Structure

- prefer clear ownership and lifetime rules
- keep interfaces small and explicit
- avoid mixing business logic, IO, and stateful side effects in one function

## Safety

- prefer RAII over manual cleanup
- avoid raw owning pointers; prefer smart pointers or stack ownership
- initialize variables immediately
- make const usage explicit for inputs and methods that do not mutate state

## Maintainability

- keep headers minimal and avoid unnecessary includes
- prefer standard library facilities before introducing custom helpers
- keep macros rare and tightly scoped
- do not add clever template abstractions without a clear need

## Verification

- compile with warnings enabled
- add or update tests for changed behavior when the project supports testing
- verify both success paths and failure paths for risky logic
