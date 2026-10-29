# Security policy

## Project boundary

This repository currently contains planning documents only. It does not collect network data or control host networking.

Future versions may inspect sensitive local network and process information, and may eventually offer network actions. Permission boundaries, least privilege, privacy, and predictable recovery are research requirements, not assumptions that have already been solved.

## Reporting a vulnerability

There is no dedicated security contact configured yet. Do not include private network captures, credentials, or sensitive host information in public issues. Until a private reporting channel is established, report only a minimal description through the repository host's private vulnerability reporting feature if available.

## Security expectations for future implementation

- Read-only observation and network-changing actions must have separate, documented boundaries.
- Any privileged component must have a narrowly scoped interface and explicit authorization model.
- User-visible actions must make their target and effect clear and handle stale state safely.
- Logs and diagnostics must avoid exposing more network or process detail than necessary.
