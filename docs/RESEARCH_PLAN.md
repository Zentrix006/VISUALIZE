# Research plan

## Purpose

Establish the user need, technical boundaries, and safety model before choosing an implementation. Keep claims tied to evidence and mark assumptions clearly.

## Research stages

### 1. Define the problem and users

Questions:

- Who is the first intended user: a desktop user, developer, administrator, or another group?
- What problem is hard to solve with current system tools?
- What information should the visual view make obvious?
- Which desktop environments and Linux distributions matter first?

Deliverable: a short problem statement, primary user profile, and prioritized use cases.

### 2. Define connection terminology and scope

Questions:

- Does “connection” mean established sockets, listening services, flows, DNS activity, or a combination?
- Should the view include inbound, outbound, local-only, IPv4, IPv6, TCP, UDP, and transient traffic?
- What grouping is most useful: process, remote endpoint, service, interface, or time?
- How should containers, namespaces, VPNs, proxies, and system services appear?

Deliverable: a glossary and an explicit in-scope/out-of-scope list.

### 3. Study user workflows and interface concepts

Questions:

- How does a user find an unfamiliar or unwanted connection?
- What details are needed before taking action?
- Which visual forms help users understand direction, grouping, and state?
- What keyboard, screen-reader, color-contrast, and small-window needs apply?

Deliverable: user flows and low-fidelity interface sketches, including an observation-only view.

### 4. Investigate Linux data sources

Questions:

- Which supported system interfaces can provide socket, process, endpoint, and state information?
- What can be read without elevated privileges, and what becomes incomplete?
- How quickly can the data change, and how should stale or racing observations be handled?
- What differs across kernel versions, distributions, containers, and network namespaces?

Deliverable: a source comparison with coverage, permissions, portability, freshness, and maintenance trade-offs. Verify details against current primary documentation during this stage.

### 5. Define control semantics and safety boundaries

Questions:

- What exactly should “disconnect” mean for each supported connection type?
- Can a single socket be ended, or would the action need to affect a process, firewall rule, interface, or route?
- What privileges would each action require?
- How will the interface show scope, consequences, errors, and recovery steps before and after an action?
- How will the design avoid applying an action to a different connection after the displayed state changes?

Deliverable: an action matrix and threat model. No control mechanism is selected until the evidence and user need are clear.

### 6. Evaluate architecture and technology options

Questions:

- Which UI toolkit and language best fit the target users and deployment model?
- Should data collection run in-process or through a small privileged helper?
- What is the smallest secure interface between the UI and any helper?
- How should collection, normalization, presentation, and control be separated?

Deliverable: an architecture decision record (ADR) comparing options and documenting the choice.

### 7. Build a safe prototype

Start with synthetic or recorded, sanitized data. Validate the visual model and information hierarchy without requiring elevated privileges or changing host networking.

Deliverable: a prototype, usability notes, and a list of changes needed before live observation.

### 8. Validate live observation

Only after the source and permission review, implement read-only collection behind a clearly documented boundary. Check accuracy, resource use, unsupported cases, and privacy implications.

Deliverable: a tested observation-only build with known limitations documented.

### 9. Reassess controls before implementation

Review the action matrix with realistic failure cases and user workflows. Implement a narrow control only if its effect is predictable, authorized, and recoverable. Keep observation usable when control is unavailable.

Deliverable: reviewed control specification, tests, and recovery guidance before enabling any action.

### 10. Prepare a release

Review supported platforms, packaging, permissions, accessibility, privacy, security reporting, and installation/removal behavior.

Deliverable: release checklist, user documentation, and a clear statement of supported environments and limitations.

## Evidence and decision records

For each research note, record:

- Question and date
- Sources consulted, favoring primary documentation and reproducible experiments
- Finding and confidence
- Constraints and known gaps
- Decision made, or why it remains open

Store durable decisions as `docs/adr/NNNN-short-title.md`. Keep user research anonymized and do not commit personal network identifiers, packet captures, credentials, or private host data.

## Open questions

- Who is the primary user for the first usable release?
- What exact activity belongs in the connection view?
- What does the user expect “disconnect” to do, and should it be temporary or persistent?
- Which Linux distributions and desktop environments are initial support targets?
- Which language, UI toolkit, and packaging format fit those users?
