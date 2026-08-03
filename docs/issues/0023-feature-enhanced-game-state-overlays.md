---
id: "0023"
title: "Feature: Enhanced Game State Overlays"
type: "feature"
status: "in-progress"
assignee: "startup-ui-dev"
labels: "feature"
due: "2026-08-15"
created: "2026-08-02"
updated: "2026-08-03"
started: "2026-08-03T03:28:42"
---

### Value Case
**Target Audience:** Casual Players.
**Metric:** Engagement / Clarity of State.
**Reasoning:** The vision emphasizes a "no-frills" but high-quality experience. Enhancing the end-game states makes the 3-minute loop feel like a complete cycle, highlighting the persistent scores which is the primary way players stay engaged after one run.

### Tasks
- Refine `STATE.WON` and `STATE.LOST` rendering in `src/game.js`.
- Center high-contrast text and include final score vs highest known record.
- Add a 'pause' or transition effect when shifting states to mimic arcade cabinet behavior.

> 2026-08-02 — Acceptance criteria:
- Implement enhanced game state overlays
- Display score, lives, and status overlays
Size: Medium
Due date: 2026-08-15

> 2026-08-03 — Prepare enhanced game state overlays for power-pellet and ghost edible states. This is part of the next cycle's focus on completing ghost AI and player feedback.

> 2026-08-03 — Starting work on feature #0023: Enhanced Game State Overlays. This serves the success criterion 'Score, lives and level shown live; game over and level-up states work.'
