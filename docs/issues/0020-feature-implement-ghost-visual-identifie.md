---
id: "0020"
title: "Feature: Implement Ghost Visual Identifiers & State Logic"
type: "feature"
status: "todo"
assignee: "startup-senior-dev"
labels: "feature"
due: "2026-08-15"
created: "2026-08-02"
updated: "2026-08-03"
---

### Value Case
Target Audience: **Retro-Gaming Fans**
Metric: Engagement & Polish.
By giving each ghost a distinct color (Red, Pink, Cyan, Orange) and a 'scared' visual state when `power_up` is active, we fulfill the requirement for "distinct behaviors" in a way that makes it visually obvious to players who care about the mechanics.

### Tasks
- Assign unique colors/shades to each of the 4 ghost types based on their movement logic.
- Implement a visual change (e.g., turning gray or blue) when `power_up` is true.
- Update `src/game.js` to handle these color shifts in the drawing loop.

> 2026-08-02 — Acceptance criteria:
- Implement visual identifiers for ghosts
- Implement ghost state logic (normal, frightened, eaten)
- Visuals update correctly based on state
Size: Medium
Due date: 2026-08-15

> 2026-08-03 — Prioritize implementation of power-pellet interaction system where ghosts flee and become edible for a limited time. This completes the ghost AI behaviors and is the highest priority for the next cycle to meet the playable core loop success criteria.
