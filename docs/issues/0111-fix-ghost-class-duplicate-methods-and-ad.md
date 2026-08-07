---
id: "0111"
title: "Fix Ghost class duplicate methods and add GhostVisual enum; update ghost visual tests"
type: "bug"
status: "backlog"
assignee: ""
labels: "feature,bug"
due: ""
created: "2026-08-07"
updated: "2026-08-07"
objective: "Missing tests and implementation for ghost visual identifiers and state logic"
accept: "pytest tests/test_ghost_visuals.py"
---

Fix the duplicate __init__ and methods in the Ghost class in src/backend/ghost_ai.py to ensure correct ghost state management.
Add a proper GhostVisual enum with members BLINKY, PINKY, INKY, CLYDE, FRIGHTENED, EYES_UP, EYES_DOWN, EYES_LEFT, EYES_RIGHT to src/backend/ghost_ai.py.
Update tests/test_ghost_visuals.py to import and test the new GhostVisual enum correctly.

This addresses missing implementation and tests for ghost visual identifiers and state logic, serving cards #0049 and #0050.
