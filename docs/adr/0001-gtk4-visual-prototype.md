# ADR 0001: Build the first visual prototype with GTK4

- **Status:** Accepted for the prototype
- **Date:** 2026-10-29

## Context

VISUALIZE is intended to become a Linux desktop application. The first milestone is to refine the system-centered connection map, service details, and dark visual style before integrating live connection data or network controls.

## Decision

Build the first interactive UI in Python using GTK4 and PyGObject. Use synthetic data with documentation-only domains and reserved example IP addresses. Show a clear demo-data indicator. The disconnect control changes only the local prototype state.

## Consequences

- The prototype runs as a native GTK4 desktop window without a browser.
- The UI can be iterated independently from Linux data collection and privileged network actions.
- Development requires GTK4, the GTK4 introspection package, PyGObject, and PyCairo from the Linux distribution.
- The prototype is not evidence that location resolution or connection attribution is reliable; those remain research tasks.
- Revisit the implementation stack before production packaging if live data collection changes the architecture.
