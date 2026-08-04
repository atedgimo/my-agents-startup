---
id: "0069"
title: "Bug: Investigate and fix import errors and app initialization NameError blocking acceptance tests for card #0050"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-04"
updated: "2026-08-04"
objective: "Four ghosts with distinct behaviours (chase, ambush, patrol, random), and power-pellets that make them flee and edible for a limited time."
accept: "pytest -q tests/test_ghost_visuals.py"
---

Acceptance tests for card #0050 fail due to import errors and app initialization NameError in src/backend/main.py.

These errors prevent the app from starting and the tests from running.

Steps to reproduce:
- Run acceptance test for card #0050
- Observe import errors and NameError

Expected:
- No import errors
- App initialized correctly
- Acceptance tests pass

This bug blocks completion of card #0050 and the release.

Assign to senior dev to investigate and fix.
