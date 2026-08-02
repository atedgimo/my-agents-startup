---
id: "0022"
title: "Feature: Visual Juice & Feedback Mechanisms"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-15"
created: "2026-08-02"
updated: "2026-08-02"
---

### Value Case
**Target Audience:** Casual Players.
**Metric:** User Retention/Retention of Flow.
**Reasoning:** Since audio is forbidden, visual "pops" and a "glow" on the player are essential to communicate state changes (like power-ups) and successful interactions (eating pellets). This ensures the game feels responsive and polished without adding complex mechanics.

### Tasks
- Implement a "pulse" effect or frame-buffer for pellet collection in `src/game.js`.
- Add a visual indicator (aura/outline) around the player when `power_up` is true.
