---
id: "0098"
title: "Add GhostVisual enum to ghost_ai.py to fix import error in ghost visual tests"
type: "bug"
status: "backlog"
assignee: ""
labels: "bug"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "playable in the browser"
accept: "pytest -q tests/test_ghost_visuals.py"
---

The tests in tests/test_ghost_visuals.py expect a GhostVisual enum with members like BLINKY, PINKY, INKY, CLYDE, FRIGHTENED, EYES_UP, EYES_DOWN, EYES_LEFT, EYES_RIGHT. However, this enum is missing in src/backend/ghost_ai.py, causing import errors.

This card adds the GhostVisual enum with the expected members to ghost_ai.py to fix the import error and allow the tests to run.

This serves the objective: "playable in the browser" by ensuring ghost visual identifiers and state logic are correctly implemented and tested.

Acceptance test:
pytest -q tests/test_ghost_visuals.py

This command currently fails due to the missing GhostVisual enum and will pass when this card is implemented.
