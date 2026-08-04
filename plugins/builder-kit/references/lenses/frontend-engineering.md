# Frontend Engineering Lens

- Which components/tokens/hooks/clients already own this behavior?
- Which state is server-owned, URL-owned, form-local, or shared client state?
- Are requests bounded, cancellable, environment-correct, and race-safe?
- Can a shared component remain domain-neutral through props/composition?
- What happens on direct entry, refresh, back/forward navigation, small screens, and supported themes?
- Which accessibility behavior belongs inside the reusable component contract?
- What unit/component/end-to-end and rendered-state evidence is needed?

Prefer existing patterns, typed boundaries, narrow data, and a central shared owner over page-specific duplication.
