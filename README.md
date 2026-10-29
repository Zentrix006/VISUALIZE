<div align="center">

# VISUALIZE

### See what your system is connected to.

**A Linux desktop project for visualizing the system's live outbound internet connections, with the long-term goal of managing selected connections from the same view.**

![Work in progress](https://img.shields.io/badge/status-work%20in%20progress-f0ad4e?style=for-the-badge)
![Linux](https://img.shields.io/badge/target-Linux-5577cc?style=for-the-badge&logo=linux&logoColor=white)

## 🚧 Work is underway — coming soon

We’re researching the problem and building the first GTK4 prototype. **There’s no packaged download yet.** The current preview uses synthetic data and does not inspect or change your network.

</div>

---

## The idea

Network activity can be difficult to understand when it is spread across process lists and command-line tools. VISUALIZE aims to bring that activity into one approachable desktop view, with the Linux system at the center of a live connection map.

Dynamic links represent connections initiated by the system to remote internet services. Selecting a service node should reveal details about that service and its location. In a future version, users may be able to manage selected connections from the map; the exact meaning and scope of “disconnect” is still being researched.

## Project status

| Stage | Status |
| --- | --- |
| Research and product scope | **In progress** |
| GTK4 visual prototype | **In progress** |
| Read-only connection view | Planned |
| Carefully scoped connection controls | Planned |

Follow the [research plan](docs/RESEARCH_PLAN.md), [roadmap](docs/ROADMAP.md), and [initial findings](docs/research/INITIAL_FINDINGS.md). Inbound connections may be considered separately; they are not part of the currently described first view.

## Product principles

- Make active connections understandable at a glance, with details available when needed.
- Show useful context such as direction, endpoint, owning process when available, and current state.
- Keep observation separate from control. Viewing data should not modify network behavior.
- Make future disconnect or restriction actions explicit, scoped, and reversible where possible.
- Explain permission requirements and the effect of an action before it happens.
- Treat missing, stale, or unavailable system information as unknown rather than guessing.
- Make the interface accessible to people beyond network specialists.

## Scope under research

- Linux desktop as the initial target.
- Inbound and outbound system-associated connections; exact scope is still open.
- How connections map to processes and services, including cases where ownership is unknown.
- Visual exploration, filtering, and connection details.
- Safe and clear control behavior, permissions, failure handling, and recovery.

## Development approach

Work proceeds through evidence-backed stages. Each stage should document findings, decisions, and open questions before the next stage is treated as settled. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose research and implementation changes.

## Follow along

Star or watch the repository for updates. **VISUALIZE is coming soon.**

## Run the source prototype

The prototype requires Linux, Python 3, GTK 4, PyGObject, and PyCairo. On Debian or Ubuntu, install the system packages first:

```sh
sudo apt install python3 python3-gi python3-cairo gir1.2-gtk-4.0
```

Then run it from the repository root:

```sh
PYTHONPATH=src python3 -m visualize
```

All displayed connections, traffic values, and locations are sample data. The **Simulate disconnect** button only changes the preview state.

Run the current unit tests in a headless session with:

```sh
xvfb-run -a env PYTHONPATH=src /usr/bin/python3 -m unittest discover -s tests -v
```

---

<div align="center">

*Project in progress · Linux desktop · Preview to come*

</div>
