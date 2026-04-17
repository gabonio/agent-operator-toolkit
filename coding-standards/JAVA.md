# Generic Java Guardrails

Use this for Java services, libraries, and backend applications.

## Structure

- keep controllers or handlers thin
- place business logic in well-named services
- keep data access and external integrations separate from core decision logic

## Safety

- validate inputs at the edge of the system
- prefer constructor injection and explicit dependencies
- avoid leaking internal stack details in user-facing errors
- use standard libraries and mature frameworks before adding new dependencies

## Maintainability

- choose descriptive class and method names
- keep classes focused on one responsibility
- avoid hidden mutable global state
- prefer immutable data where practical

## Verification

- add or update unit tests for service logic
- include at least one negative-path test when behavior changes
- run the project's build and test commands before declaring success
