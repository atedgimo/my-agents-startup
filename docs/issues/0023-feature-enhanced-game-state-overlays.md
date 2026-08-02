---
id: "0023"
title: "Feature: Enhanced Game State Overlays"
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
**Metric:** Engagement / Clarity of State.
**Reasoning:** The vision emphasizes a "no-frills" but high-quality experience. Enhancing the end-game states makes the 3-minute loop feel like a complete cycle, highlighting the persistent scores which is the primary way players stay engaged after one run.

### Tasks
- Refine `STATE.WON` and `STATE.LOST` rendering in `src/game.js`.
- Center high-contrast text and include final score vs highest known record.
- Add a 'pause' or transition effect when shifting states to mimic arcade cabinet behavior.
