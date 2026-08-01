# Tech Lead

1. **[SETUP] Initialize SQLite Database Schema (Habits, Logs, Journal)**
    *   **Type:** Backend/Data Setup
    *   **Labels:** `backend`, `data`, `setup`
    *   **Body Summary:** Set up the three core tables (`Habits`, `HabitLogs`, `JournalEntries`) with all necessary fields and constraints (e.g., unique constraint on habit logs).

2. **[BACKEND] Implement Habit Management API (CRUD)**
    *   **Type:** Backend Feature
    *   **Labels:** `backend`, `task`
    *   **Body Summary:** Implement endpoints for creating, listing, and updating habits (`POST /api/v1/habits`, `GET /api/v1/habits`).

3. **[BACKEND] Implement Habit Logging & History API**
    *   **Type:** Backend Feature (Core)
    *   **Labels:** `backend`, `task`
    *   **Body Summary:** Implement the core logging mechanism (`POST /api/v1/logs`) and history retrieval endpoint, including date range filtering.

4. **[BACKEND] Implement Journaling API (CRUD)**
    *   **Type:** Backend Feature
    *   **Labels:** `backend`, `task`
    *   **Body Summary:** Implement endpoints for managing journal entries (`POST /api/v1/journal`, `GET /api/v1/journal?date={date}`).

5. **[FRONTEND] Setup Core SPA Structure and Navigation Shell**
    *   **Type:** Frontend Foundation
    *   **Labels:** `frontend`, `task`
    *   **Body Summary:** Establish the React/Vite shell, routing, basic UI structure (Tailwind), and a global API service layer to communicate with the local backend.

6. **[BACKEND] Implement Local LLM Processing API Endpoint**
    *   **Type:** Backend Advanced Feature
    *   **Labels:** `backend`, `advanced`, `task`
    *   **Body Summary:** Integrate the zero-cost, local AI processing endpoint (`POST /api/v1/llm/process`) using `llama-cpp-python`.

*(Note: The final step of connecting Frontend components to these APIs is implicitly handled by subsequent tasks following this sequence.)*
