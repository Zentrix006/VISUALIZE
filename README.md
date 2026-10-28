# VISUALIZE

> Project name. Product scope is still being researched.

**A Linux desktop tool for seeing the network connections associated with a system and, eventually, managing selected connections through a clear visual interface.**

The project starts with research and product definition. It will not change network traffic until the behavior, permissions, and recovery paths have been designed and reviewed.

## Project description

Network activity is often shown as text, counters, or process lists. This project explores a visual way to understand which connections are active on a Linux system, where they lead, and which local applications or services are associated with them. The longer-term goal is to let a user deliberately disconnect or restrict a selected connection from that view.

The first research pass will define what counts as a connection, which kinds of traffic are in scope, how process and endpoint information can be collected, and what “disconnect” should do. Those decisions will shape the interface and implementation. Until then, this repository is a planning and research foundation, not a working network controller.

## Current status

**Stage 0 — project framing and research planning.** No network data is collected or changed by this project yet. See [the research plan](docs/RESEARCH_PLAN.md) and [the roadmap](docs/ROADMAP.md).

## Product principles

- Make active connections understandable at a glance, with details available when needed.
- Show enough context to identify a connection, such as direction, endpoint, owning process when available, and current state.
- Keep observation separate from control. Viewing data should not modify network behavior.
- Make any future disconnect or restriction action explicit, scoped, and reversible where possible.
- Explain permission requirements and the effect of an action before it happens.
- Treat missing, stale, or unavailable system information as unknown rather than guessing.
- Prefer a useful, accessible interface over a dense network-analyst-only display.

## Scope to investigate

- Linux desktop as the initial target.
- System-associated connections, including inbound and outbound activity; exact scope is a research decision.
- Mapping connections to processes and services, including how to represent cases where ownership cannot be determined.
- Visual exploration, filtering, and connection details.
- Possible controls for ending or restricting selected activity, with a clear distinction between those actions.
- Permission boundaries, failure handling, auditability, and recovery.

## Development approach

Work proceeds through evidence-backed stages. Each stage should leave a written result, decisions, and open questions before the next stage is treated as settled. See [Research plan](docs/RESEARCH_PLAN.md) for the questions and evidence to gather, and [Roadmap](docs/ROADMAP.md) for the proposed sequence of deliverables.

### Initial development practices

- Keep research notes and decisions in `docs/` so design choices are traceable.
- Record unresolved questions instead of quietly turning assumptions into requirements.
- Keep changes focused and reviewable; use branches and pull requests when collaborating.
- Add tests and automated checks when implementation begins, based on the chosen stack.
- Do not run privileged commands or alter host networking as part of ordinary development.

## Repository layout

```text
.
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .gitignore
└── docs/
    ├── RESEARCH_PLAN.md
    └── ROADMAP.md
```

## Contributing

The project is in its planning stage. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Research findings should include the question, sources or evidence, conclusion, confidence, and remaining uncertainty. Do not include private network data, credentials, or identifying packet captures in the repository.

## Security

Security and permission design are core research topics because future versions may interact with host networking. Please see [SECURITY.md](SECURITY.md) for the current reporting guidance and project boundary.

## License

No license has been selected yet. Until one is added, reuse and redistribution are not granted by this repository.
