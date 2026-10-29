# Initial findings

**Status:** Early project framing  
**Date:** 2026-10-29

## Confirmed direction

- Linux is the intended initial platform.
- The map should keep the local system at the center.
- Dynamic links should represent internet connections initiated by the local system.
- Remote service nodes should reveal service details and location when selected.
- The longer-term goal includes a way to disconnect selected activity through that interface.
- Research and documentation should precede implementation.

## Visual direction

The supplied reference image establishes a dark, high-contrast network map with a central hub, visibly active links, endpoint nodes, and a compact status panel. For this project, the central hub is the user's Linux system; remote nodes represent services reached by the system. The image is a style and interaction reference, not a literal network topology specification.

## Prototype status

The first source prototype uses Python with GTK4 and synthetic connection data. It demonstrates the dark map, selectable service nodes, a service-detail panel, approximate location labels, and a simulated disconnect action. It does not read system connections, resolve live service locations, or change network behavior.

## Repository baseline

- The GitHub repository is `Zentrix006/VISUALIZE`.
- At the time of this note, its `main` branch contains an initial commit with a short README.
- No application implementation or stack choice has been established in the repository yet.

## Not yet established

- Which connection types, protocols, and lifetimes should appear in the first view.
- Whether inbound connections belong in a later view or release.
- How a remote endpoint should be resolved to a recognizable service and location, and how uncertainty should be shown.
- Whether a disconnect action targets one socket, an application, a service, or a wider network control.
- Which users, distributions, and desktop environments are the first target.
- How any future collection or control should handle permissions, privacy, and recovery.

## Next research steps

Use [the research plan](../RESEARCH_PLAN.md) to resolve user needs and terminology, then compare current Linux data sources and permission models using primary documentation. Do not treat the open questions above as settled requirements.
