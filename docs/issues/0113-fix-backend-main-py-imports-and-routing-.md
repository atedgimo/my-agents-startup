---
id: "0113"
title: "Fix backend main.py imports and routing for ghost AI feature"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: "2024-08-15"
created: "2026-08-08"
updated: "2026-08-08"
objective: "Feature: Implement Ghost Visual Identifiers & State Logic"
accept: "pytest tests/acceptance/test_ghost_visuals.py"
---

The current backend main.py references non-existent modules src.backend.api and src.backend.ghosts, causing import errors and blocking the ghost visual identifiers and state logic feature (#0020).

This card will fix the imports and properly register the ghost AI routes and logic in main.py to unblock the feature implementation.

objective: "Feature: Implement Ghost Visual Identifiers & State Logic"
accept: "pytest tests/acceptance/test_ghost_visuals.py"
