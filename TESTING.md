# Testing

This branch is reserved for test planning and validation work. The repository currently has no application code or chosen implementation stack, so there are no automated tests to run yet.

## Current baseline

- Confirm the project is still planning-only before treating a missing test suite as a failure.
- Keep experiments isolated from the host's active network configuration.
- Use synthetic or sanitized fixtures for network and process data.
- Do not require root privileges for ordinary unit tests or CI jobs.

## Test layers to add with implementation

1. **Unit tests:** parsing, normalization, filtering, and state handling using fixed fixtures.
2. **Integration tests:** collection and permission behavior in a controlled environment with documented Linux prerequisites.
3. **UI tests:** connection discovery, detail views, filtering, accessible navigation, and stale-data states.
4. **Control tests:** only after control behavior is specified; use isolated network namespaces or another disposable environment and verify both the intended effect and recovery.
5. **Release checks:** supported distribution and packaging checks, permission review, and a clear summary of known coverage gaps.

When the language and UI toolkit are selected, replace this outline with reproducible commands and CI configuration. Every new test should state what it covers and any environment assumptions it makes.
