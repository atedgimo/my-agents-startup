---
id: "0024"
title: "feat: integrate frontend with backend for score persistence"
type: "feature"
status: "backlog"
assignee: ""
labels: ""
due: ""
created: "2026-08-02"
updated: "2026-08-02"
---

The frontend (`src/game.js`) currently does not make any network requests to the backend. To meet the requirement of "High scores persist across page reloads," we need a bridge between the game loop and the FastAPI server.

**Plan:**
1. Define an API client or a simple fetch wrapper in `src/game.js`.
2. Connect the `score` variable update to a call to `/submit-score`.
3. Optionally, load initial high scores on page load using `/scores`.
