# ADR 0002: Frontend-Backend Integration for Score Persistence

## Context
The project requires the frontend game to persist high scores by communicating with the backend API. The backend is implemented in FastAPI and exposes endpoints for submitting and retrieving scores.

## Decision
We will implement a dedicated API client module in the frontend JavaScript (`src/game.js` or a new module) that uses `fetch` to interact with the backend endpoints.

### Justification
- Keeps the frontend code modular and maintainable.
- Allows easy updates to API endpoints or request headers in one place.
- Aligns with the principle of Single Source of Truth (SSoT) for API contracts.

## Consequences
- The frontend will be able to submit and retrieve scores, enabling persistence across page reloads.
- Requires additional testing to ensure API calls succeed and handle errors gracefully.

## Principle: Single Source of Truth (SSoT)
Define a clear contract between frontend and backend to prevent integration bugs and ease maintenance.