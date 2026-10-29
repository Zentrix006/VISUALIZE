# Roadmap

This roadmap is provisional. Stages are gated by research findings; dates and implementation choices are intentionally not set yet.

## Stage 0 — repository and project framing

- [x] Create project overview and development documentation.
- [x] Define a research-first workflow.
- [ ] Confirm primary users and first use cases.
- [ ] Choose a public project name and license.

## Stage 1 — product and platform research

- [ ] Define connection terminology and boundaries.
- [ ] Review Linux data sources and permission requirements.
- [ ] Compare user workflows and visual models.
- [ ] Write an initial threat model and control action matrix.
- [ ] Record architecture choices as ADRs.

## Stage 2 — interaction prototype

- [x] Create a GTK4 visual prototype using synthetic data.
- [ ] Review connection discovery, detail, filtering, and accessibility.
- [ ] Validate whether the visual model communicates state and direction.

## Stage 3 — read-only Linux observation

- [ ] Select implementation stack and supported environment baseline.
- [ ] Implement collection and normalization with no network-changing actions.
- [ ] Document permissions, missing-data behavior, and platform gaps.
- [ ] Add automated checks and test fixtures.

## Stage 4 — carefully scoped connection controls

- [ ] Reconfirm what users mean by disconnecting a connection.
- [ ] Design the narrowest safe action and its permission boundary.
- [ ] Add confirmation, stale-state protection, error handling, and recovery guidance.
- [ ] Validate actions in an isolated environment before host use.

## Stage 5 — packaging and first release

- [ ] Select and document supported distributions and installation methods.
- [ ] Review accessibility, privacy, and security posture.
- [ ] Prepare user documentation and release notes.
- [ ] Publish only after support boundaries and limitations are clear.
