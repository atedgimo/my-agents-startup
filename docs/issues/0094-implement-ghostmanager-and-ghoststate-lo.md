---
id: "0094"
title: "Implement GhostManager and GhostState logic for ghost visual identifiers and states"
type: "feature"
status: "todo"
assignee: "startup-backend-python-dev"
labels: "feature"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "Ensure ghost visual identifiers and state logic are implemented and tested correctly"
accept: "pytest -q tests/test_ghost_visuals.py"
---

The current ghost_ai.py has a Ghost class but the tests and implementation for ghost visual identifiers and state logic are incomplete or inconsistent with the existing ghost_visuals.py and its tests.

We need to:
- Implement or fix GhostManager and GhostState classes to manage multiple ghosts with their states and visual identifiers.
- Ensure ghost states include IDLE, CHASE, FRIGHTENED, FLEE, EATEN, AMBUSH, PATROL, RANDOM.
- Add or fix tests to cover ghost visual identifiers and state transitions, including power pellet activation and edible state timing.

This serves the objective: "Ensure ghost visual identifiers and state logic are implemented and tested correctly".

Acceptance:
pytest -q tests/test_ghost_visuals.py

This will unblock bug #0050 and align implementation with tests.

> 2026-08-05 — Assigning to new backend/full-stack developer to implement GhostManager and GhostState logic for ghost visual identifiers and states.
