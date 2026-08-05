# ADR 0004: Frontend-Backend Integration for Score Persistence

## Context
The product requires that high scores persist across page reloads, which necessitates a reliable connection between the frontend game logic and the backend API that stores scores.

Currently, the backend exposes endpoints to submit and retrieve scores, but the frontend game logic (`src/game.js`) does not call these endpoints.

## Decision
We will implement API calls in the frontend to:
- Submit the player's score to the backend when the game ends.
- Retrieve and display the high scores from the backend when the game loads.

This integration ensures that the high scores are persistent and shared across sessions.

## Consequences
- The frontend codebase will include asynchronous fetch calls to the backend API.
- The backend API must remain stable and performant to serve these requests.
- Testing will need to cover the full integration path.

## Principle Explainer
**Separation of Concerns and Integration:**
The frontend handles user interaction and rendering, while the backend manages data persistence and business logic. Clear API contracts and integration points between frontend and backend ensure maintainability and scalability.

---

_By startup_architect on 2026-08-03_
