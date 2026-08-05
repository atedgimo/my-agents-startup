---
id: "0085"
title: "Implement frontend API calls to submit and retrieve high scores"
type: "feature"
status: "backlog"
assignee: ""
labels: "feature"
due: ""
created: "2026-08-05"
updated: "2026-08-05"
objective: "High scores persist across page reloads"
accept: "pytest tests/acceptance/test_scores_api.py"
---

The frontend game logic currently does not communicate with the backend API for score persistence. This task is to add asynchronous fetch calls in `src/game.js` to:

- Submit the player's score to the backend when the game ends.
- Retrieve and display the high scores from the backend when the game loads.

This is critical to meet the success criterion: "High scores persist across page reloads" from BOARD_BRIEF.md.

Acceptance criteria:
- The frontend successfully posts scores to the backend.
- The frontend fetches and displays the high score list on game load.

This will close the gap between frontend and backend integration for score persistence.
