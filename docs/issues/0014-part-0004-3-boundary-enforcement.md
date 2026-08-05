---
id: "0014"
title: "[part] #0004.3 Boundary Enforcement"
type: "feature"
status: "in-progress"
assignee: "startup-senior-dev"
labels: ""
due: "2026-08-14"
created: "2026-08-02"
updated: "2026-08-05"
started: "2026-08-04T19:46:23"
---

Sub-task of #0004. Ensure player cannot "jitter" or phase through corners by implementing stricter grid-aligned movement constraints.
Acceptance Criteria:
1. Player remains in the center of the tile during turn transitions.
2. No 'corner cutting' is possible unless explicitly allowed by game logic.
Size: S

> 2026-08-04 — Starting implementation of card #0014 Boundary Enforcement.

> 2026-08-05 — Implemented boundary enforcement in collision.py. The CollisionDetector class now treats out-of-bounds as walls and provides methods to check movement validity and detect collisions with walls, pellets, power pellets, and ghosts.

> 2026-08-05 — Acceptance test for boundary enforcement exists but the current Player.move_right method wraps around instead of enforcing boundaries. This is why the card is stuck in review. The implementation must be changed to prevent moving beyond the boundary, not wrap around.
