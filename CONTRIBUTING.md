# Contributing

Thanks for helping shape the project. It is currently in the research and planning stage, so questions, evidence, and careful scope proposals are especially useful.

## Before making a change

- Check the README, research plan, and roadmap for current scope.
- For a new technical or product direction, explain the user need and evidence.
- For substantial decisions, propose an ADR in `docs/adr/` rather than burying the decision in implementation details.
- Do not add real host network data, personal identifiers, credentials, or unredacted packet captures.

## Changes

- Keep each change focused and explain its purpose in the commit or pull request.
- Mark unverified statements and open questions as such.
- Link primary documentation or reproducible evidence for technical findings.
- Add or update checks when code is introduced; describe what was run in the change summary.
- Never make ordinary development or automated checks require elevated privileges or modify the developer's live network configuration.

## Pull requests

Include the problem being addressed, the approach, evidence or screenshots where useful, checks performed, and any open limitations. For changes affecting permissions or network control, include the exact action scope and recovery behavior.
