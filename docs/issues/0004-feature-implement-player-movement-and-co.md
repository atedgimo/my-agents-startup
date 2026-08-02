---
id: "0004"
title: "[Feature] Implement Player Movement and Collision Detection"
type: "feature"
status: "review"
assignee: "startup_senior_dev"
labels: "feature"
due: "2026-08-15"
created: "2026-08-01"
updated: "2026-08-02"
---

### Context
The current frontend renders the maze and pellets (as seen in #0003), but there is no interactivity yet. This issue focuses on making Pac-Man moveable within those bounds.

### Requirements / Acceptance Criteria
1. **Input Handling:** Map arrow keys (Up, Down, Left, Right) to movement.
2. **Collision Detection:** Implement wall collision logic so the player cannot pass through walls in the maze.
3. **Core Movement:** Smooth movement of the "Pac-Man" character in the game world.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

### Technical Notes
- Check `src/game.js` for existing entity definitions.
- Ensure collision detection is efficient enough to maintain 60 FPS.

> 2026-08-01 — Refining card: split into [part] Movement and [part] Collision Detection logic. Asking senior dev for technical breakdown.

> 2026-08-02 — [Pulse Check] Verified in-progress by senior_dev. Currently implementing movement vectors and wall checks in src/game.js. Stay in in-progress until logic is complete.
