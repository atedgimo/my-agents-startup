# ADR 0005: Backend Score Submission and Retrieval API

## Context
The backend needs to provide a stable API for the frontend to submit player scores and retrieve the high score list. This is essential for the feature "High scores persist across page reloads".

## Decision
We have implemented two endpoints:
- POST `/submit-score`: Accepts a JSON payload with a score integer, validates it, appends it to the in-memory list, keeps the top 10 scores, and persists them to a JSON file.
- GET `/scores`: Returns the current list of high scores.

The scores list is protected by a threading lock to ensure thread safety.

## Consequences
- The backend must ensure the scores file is accessible and writable.
- The API is simple and stateless, suitable for scaling with a shared storage mechanism if needed.
- The frontend can rely on these endpoints for score persistence.

## Principle Explainer
**Thread Safety and Data Persistence:**
When multiple requests can modify shared data, synchronization (locking) is crucial to avoid race conditions. Persisting data to a file ensures durability beyond process lifetime.

---

_By startup_architect on 2026-08-03_
