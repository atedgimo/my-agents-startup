---
id: "0075"
title: "Add automated tests for ghost visual identifiers and state logic"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug,tests"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Bug: Missing tests and implementation for ghost visual identifiers and state logic"
accept: "pytest tests/test_ghost_visuals.py"
---

Add unit tests to verify the ghost visual identifiers and state update logic in the backend.

Tests should cover:
- Ghost state transitions when power_up_active is True or False
- Correct visual identifiers returned for each ghost state ('normal', 'frightened', 'eaten')
- GhostManager updates and returns correct visuals

This completes bug #0050 by ensuring ghost logic is tested and verified.
