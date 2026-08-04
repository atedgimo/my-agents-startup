---
id: "0053"
title: "Enhance Visual Feedback and UI Clarity for Lives, Power-Ups, and Game States"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-12"
created: "2026-08-04"
updated: "2026-08-04"
objective: ""
accept: ""
---

Improve the game UI to clearly show:
- Player lives remaining.
- Power-pellet active state with ghost fleeing animation.
- Smooth transitions and overlays for game start, level clear, and game over states.

Value Case:
- Enhances user experience and accessibility by providing clear visual cues.
- Aligns with success criteria for live score, lives, level shown, and game state overlays.

Acceptance Criteria:
- Lives count is visible and updates correctly.
- Ghosts visibly change behavior and color when power-pellet is active.
- Game state overlays appear correctly on game over and level clear.

accept: curl -sf http://localhost:8000/api/ui-feedback-test | jq -e '.uiCorrect == true'

objective: "Score, lives and level shown live; game over and level-up states work."
