---
id: "0021"
title: "Feature: Ghost Identity & State Visuals"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-15"
created: "2026-08-02"
updated: "2026-08-02"
---

### Value Case
**Target Audience:** Retro-Gaming Fans & Casual Players.
**Metric:** Polish / Engagement.
**Reasoning:** By assigning unique colors to each ghost behavior and a "scared" state, we satisfy the requirement for distinct behaviors while providing necessary visual feedback in place of audio (which is out of scope).

### Tasks
- Define a color palette for the 4 ghosts (Chase, Ambish, Patrol, Random) in `src/game.js`.
- Implement logic to change ghost colors and add a "pulse" effect when `power_up` is true.
- Update the drawing loop to render these states correctly.
