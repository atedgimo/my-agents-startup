---
id: "0110"
title: "Implement boundary enforcement for player movement to prevent out-of-bounds moves"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-14"
created: "2026-08-05"
updated: "2026-08-05"
objective: "boundary enforcement for player movement"
accept: "pytest tests/test_player_movement_kinematics.py -k 'test_boundary_enforcement'"
---

The current player movement implementation wraps around when reaching the boundary instead of enforcing boundaries as required by card #0014.

Update the player movement logic to prevent moving beyond the maze boundary (e.g., x >= 19 should stop at 18, not wrap to 1).

This fixes the boundary enforcement feature so it passes the acceptance test defined in #0014.
