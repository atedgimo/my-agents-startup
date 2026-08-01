---
id: "0005"
title: "[Feature] Implement Pellet Collection and Scoring"
type: "feature"
status: "in-progress"
assignee: "startup_ui_dev"
labels: "feature"
due: "2026-08-20"
created: "2026-08-01"
updated: "2026-08-01"
---

### Context
While movement is the first step, players need to interact with the environment. This task implements the collection of pellets to update the player's score and decrement the remaining pellet count.

### Requirements / Acceptance Criteria
1. **Collision Detection (Pellets):** Detect when Pac-Man's coordinates overlap with a pellet's location.
2. **Scoring System:** Increment the user's score by a fixed amount upon pellet consumption.
3. **State Update:** Remove the collected pellet from the game state so it doesn't reappear.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

> 2026-08-01 — Refining card: split into [part] Collision Detection and [part] Pellet Collection logic.

> 2026-08-01 — Starting work on Pellet Collection and Scoring. I will implement the scoring system and the logic to remove pellets from the game state when "collected".

> 2026-08-01 — Starting work on #0005. I am adding the scoring system and pellet collection logic to src/game.js.
