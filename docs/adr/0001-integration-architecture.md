# ADR 0001: Core Integration Architecture

## Context
The project requires a high-score system where scores persist across page reloads. We have a backend (`src/backend/main.py`) providing these endpoints, but the frontend (`src/game.js`) currently has no mechanism to communicate with it.

## Decision
We will use a standard `fetch` implementation within `src/game.js` to interact with the FastAPI backend. 

### Justification
- **Simplicity:** Since we are building "one page", adding complex state management for networking is overkill at this stage.
- **Standardization:** Fetch is natively supported in all modern browsers, satisfying our requirement for a simple browser experience without extra dependencies.

## Consequences
- **Pro:** Direct implementation allows quick feature completion.
- **Con:** Without a separate API layer/wrapper, changes to the backend URL or headers will require updates in multiple places in `src/game.js` if not wrapped carefully. We should implement a simple configuration object for base URLs.

## Principle: The Single Source of Truth (SSoT)
Whenever we bridge two different domains (Frontend and Backend), always define the contract clearly. While our scale is small, ensuring that the backend's JSON structure matches exactly what the frontend expects prevents "ghost" bugs in later stages.
