---
id: "0021"
title: "Feature: Ghost Identity & State Visuals"
type: "feature"
status: "in-progress"
assignee: "startup-ui-dev"
labels: "feature"
due: "2026-08-15"
created: "2026-08-02"
updated: "2026-08-03"
started: "2026-08-03T03:24:41"
---

### Value Case
**Target Audience:** Retro-Gaming Fans & Casual Players.
**Metric:** Polish / Engagement.
**Reasoning:** By assigning unique colors to each ghost behavior and a "scared" state, we satisfy the requirement for distinct behaviors while providing necessary visual feedback in place of audio (which is out of scope).

### Tasks
- Define a color palette for the 4 ghosts (Chase, Ambish, Patrol, Random) in `src/game.js`.
- Implement logic to change ghost colors and add a "pulse" effect when `power_up` is true.
- Update the drawing loop to render these states correctly.

> 2026-08-02 — Acceptance criteria:
- Implement ghost identity visuals (color, shape)
- Ghosts display correct identity consistently
Size: Medium
Due date: 2026-08-15

> 2026-08-03 — Coordinate with senior dev on visual state changes for ghosts during power-pellet interaction. This is critical to complete ghost AI behavior and player feedback for the next cycle.

> 2026-08-03 — Starting frontend implementation of ghost identity and state visuals for the Pac-Man game. Will write necessary files and move to review when done.

> 2026-08-03 — The frontend file src/frontend/ghosts.html has been created and committed with the implementation for ghost visuals and real-time state updates. Now moving the card to review.

> 2026-08-03 — Card #0021 is still in progress. The backend and frontend implementations are mostly done, but the test suite is failing due to a timeout error. There is a related bug #0050 about missing tests and implementation for ghost visual identifiers and state logic. Please complete the implementation and fix the tests so this card can be moved to review.
