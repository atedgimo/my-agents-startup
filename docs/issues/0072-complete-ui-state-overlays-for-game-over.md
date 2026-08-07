---
id: "0072"
title: "Complete UI state overlays for Game Over and Level Up"
type: "feature"
status: "in-progress"
assignee: "startup-ui-dev"
labels: "feature"
due: "2024-07-05"
created: "2026-08-05"
updated: "2026-08-07"
started: "2026-08-05T17:58:57"
objective: "playable core loop and persistent feedback"
accept: "pytest tests/acceptance/test_ui_overlays.py"
resolution: "duplicate of #0048"
---

Implement and finalize the UI state overlays for Game Over and Level Up screens. This is essential to provide persistent feedback to players and support the playable core loop.

- Design and implement Game Over overlay
- Design and implement Level Up overlay
- Ensure overlays integrate smoothly with game flow

Objective: "playable core loop and persistent feedback"
Accept: "pytest tests/acceptance/test_ui_overlays.py"

> 2026-08-05 — This card is overdue and depends on backend stability and ghost AI fixes. Please prepare to work on UI state overlays once backend issues are resolved.

**2026-08-05 18:50** — closed as a duplicate of #0048: same work, filed more than once

> 2026-08-07 — Reopened by the co-founder: done now means SHIPPED and VERIFIED. This card closed before the acceptance rule; its check currently FAILS (pytest tests/acceptance/test_ui_overlays.py). Make it pass, then close — the close then merges.
