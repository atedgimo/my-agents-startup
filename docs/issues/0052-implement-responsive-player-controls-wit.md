---
id: "0052"
title: "Implement Responsive Player Controls with Arrow and WASD Keys"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: "2026-08-10"
created: "2026-08-04"
updated: "2026-08-04"
objective: ""
accept: "pytest tests/ -q -k \"responsive or control\""
---

Add real-time player movement controls using arrow keys and WASD keys for accessibility.

- Capture keyboard input events to move Pac-Man smoothly in the maze.
- Ensure input responsiveness and no input lag.
- Integrate with existing game loop and collision logic.

Value Case:
- Improves core gameplay interaction, making the game playable end-to-end in the browser.
- Moves the success metric of "Playable end to end in a browser" forward.

Acceptance Criteria:
- Player can move Pac-Man using arrow keys and WASD keys.
- Movement respects maze boundaries and collisions.
- No console errors during input handling.

accept: curl -sf http://localhost:8000/api/player-move-test | jq -e '.success == true'

objective: "Playable end to end in a browser: arrow keys move Pac-Man"

**2026-08-04 17:31** — acceptance repaired: `pytest tests/ -q -k "responsive or control"` — planner omitted the check: responsive player controls
