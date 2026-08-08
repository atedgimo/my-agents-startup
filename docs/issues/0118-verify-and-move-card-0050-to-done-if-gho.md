---
id: "0118"
title: "Verify and move card #0050 to done if ghost visual identifiers and state logic tests pass"
type: "chore"
status: "backlog"
assignee: ""
labels: "chore"
due: ""
created: "2026-08-08"
updated: "2026-08-08"
objective: "Ensure the ghost visual identifiers and state logic feature is fully implemented and tested."
accept: "pytest tests/acceptance/test_ghost_visuals.py"
---

Acceptance tests for ghost visual identifiers and state logic exist in tests/acceptance/test_ghost_visuals.py and test the /ghosts API routes.

I have implemented the missing /ghosts API routes in src/backend/main.py to match the tests.

Objective: Ensure the ghost visual identifiers and state logic feature is fully implemented and tested.

Acceptance: pytest tests/acceptance/test_ghost_visuals.py
