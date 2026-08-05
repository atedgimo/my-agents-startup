---
id: "0093"
title: "Implement missing src.backend.ghost_ai module to fix import errors"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: "2024-06-10"
created: "2026-08-05"
updated: "2026-08-05"
objective: "Four ghosts with distinct behaviours (chase, ambush, patrol, random), and power-pellets that make them flee and edible for a limited time."
accept: "pytest tests/acceptance/test_ghost_ai.py"
---

This bug addresses the missing src.backend.ghost_ai module which is causing import errors and blocking backend tests and ghost-related cards. Fixing this will unblock multiple cards related to ghost AI behaviors and visuals.
