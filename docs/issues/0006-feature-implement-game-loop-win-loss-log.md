---
id: "0006"
title: "[Feature] Implement Game Loop & Win/Loss Logic"
type: "feature"
status: "in-progress"
assignee: "startup_senior_dev"
labels: "feature"
due: "2026-08-25"
created: "2026-08-01"
updated: "2026-08-02"
---

### Context
Once the player can move and collect pellets, the game needs a state machine to handle winning (all pellets collected), losing (collision with ghost without power-pellet), and level resets/restarts.

### Requirements / Acceptance Criteria
1. **Win Condition:** Check if all pellet items have been "consumed". If so, display a 'Level Clear' message.
2. **Loss Condition:** Detect collision between player and ghost while the 'power_up' state is inactive. Trigger a 'Game Over' screen.
3. **State Management:** Implement clear states (PLAYING, WON, LOST) to manage UI overlays and gameplay suspension.
4. **Metric moved:** Directly impacts OKR Q3: Gameplay Mechanics (KR1).

> 2026-08-02 — Moving to in-progress. Dev started on game loop and win/loss logic.

> 2026-08-02 — Senior Dev completed implementation of Game Loop & Win/Loss Logic. Backend API for high scores (FastAPI/SQLite) is live, and frontend state machine handles win/loss conditions. Moving to review.

> 2026-08-02 — Senior dev reports that the game loop and win/loss logic are complete. Moving to review.

> 2026-08-02 — Moving back as game loss transition is currently just a comment (tracked in #0008).
