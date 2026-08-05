---
id: "0097"
title: "Implement missing src.backend.ghost_visuals module with GhostManager and GhostState to fix import errors and test failures"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Implement missing src.backend.ghost_visuals module with GhostManager and GhostState to fix import errors and test failures"
accept: "pytest tests/test_ghost_visuals.py"
---

The tests in tests/test_ghost_visuals.py require a src.backend.ghost_visuals module defining GhostManager and GhostState.

This module is missing, causing import errors and blocking the release.

Implement the ghost_visuals module with the GhostManager class and GhostState enum to pass the acceptance tests and fix the bug #0050.

Assign to senior backend dev for implementation.
