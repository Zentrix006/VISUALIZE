# Initial findings

**Status:** Early project framing  
**Date:** 2026-10-29

## Confirmed direction

- Linux is the intended initial platform.
- The project is intended to make a system's internet/network connections visible through a visual interface.
- The longer-term goal includes a way to disconnect selected activity through that interface.
- Research and documentation should precede implementation.

## Repository baseline

- The GitHub repository is `Zentrix006/VISUALIZE`.
- At the time of this note, its `main` branch contains an initial commit with a short README.
- No application implementation or stack choice has been established in the repository yet.

## Not yet established

- Whether “connections” means sockets, listening services, network flows, or another unit.
- Whether the first view is inbound-only or includes inbound and outbound activity.
- Whether a disconnect action targets one socket, an application, a service, or a wider network control.
- Which users, distributions, desktop environments, and UI toolkit are the first target.
- How any future collection or control should handle permissions, privacy, and recovery.

## Next research steps

Use [the research plan](../RESEARCH_PLAN.md) to resolve user needs and terminology, then compare current Linux data sources and permission models using primary documentation. Do not treat the open questions above as settled requirements.
