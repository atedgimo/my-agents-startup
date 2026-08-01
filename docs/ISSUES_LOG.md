## [SETUP] Initialize SQLite Database Schema (Habits, Logs, Journal)

**Labels:** backend,data,setup

### Goal: Initialize the SQLite database schema.

This task involves setting up the necessary tables and constraints defined in `ARCHITECTURE.md` within the local SQLite file. This is a prerequisite for all other backend functionality.

**Acceptance Criteria:**
1.  A function/script must exist to connect to the SQLite database file (`local_data.db`).
2.  The following three tables must be created with their specified columns and constraints:
    *   `Habits`: (habit\_id, name, description, creation\_date, is\_active)
    *   `HabitLogs`: (log\_id, habit\_id, date, is\_completed, value) - Must enforce unique constraint on (`habit_id`, `date`).
    *   `JournalEntries`: (entry\_id, user\_id, date, content, related\_habit\_id)
3.  The schema initialization must be called early in the FastAPI startup process.

**Labels:** backend, data, setup

---

## [BACKEND] Implement Habit Management API (CRUD)

**Labels:** backend,task

### Goal: Implement API endpoints for managing user habits.

This task focuses on the CRUD operations for the `Habits` table using FastAPI and SQLite.

**Acceptance Criteria:**
1.  Implement a function to connect to the database and execute SQL queries safely (using parameterized statements).
2.  Create the `POST /api/v1/habits` endpoint: Must accept `{name, description}` and insert a new record into the `Habits` table, returning the new `habit_id`.
3.  Create the `GET /api/v1/habits` endpoint: Must query and return an array of all active habits (Name, Description, ID).
4.  Implement the PUT logic for updating habit details (optional but good practice to include now).

**Labels:** backend, task

---

## [BACKEND] Implement Habit Logging & History API

**Labels:** backend,task

### Goal: Implement API endpoints for logging daily progress against habits.

This task covers the core functionality of tracking habit completion.

**Acceptance Criteria:**
1.  Create `POST /api/v1/logs`: Must accept `{habit_id, date, is_completed, value}` and insert a record into `HabitLogs`. Should handle potential unique constraint violations gracefully (i.e., if the entry already exists for that habit/date).
2.  Create `GET /api/v1/logs/history`: Must accept query parameters (`habit_id`, `start_date`, `end_date`) and retrieve all corresponding records from `HabitLogs`. The response should be structured to facilitate streak calculation on the frontend.

**Labels:** backend, task

---

## [BACKEND] Implement Journaling API (CRUD)

**Labels:** backend,task

### Goal: Implement API endpoints for journal entry management.

This task covers the storage and retrieval of reflective thoughts, linking them optionally to a habit.

**Acceptance Criteria:**
1.  Create `POST /api/v1/journal`: Must accept `{date, content, related_habit_id}` and insert a new record into `JournalEntries`.
2.  Create `GET /api/v1/journal?date={date}`: Must retrieve all journal entries for a specified date.

**Labels:** backend, task

---

## [FRONTEND] Setup Core SPA Structure and Navigation Shell

**Labels:** frontend,task

### Goal: Build the core Single Page Application (SPA) structure and navigation.

This task establishes the foundational frontend shell using React/Vite, ensuring it can load locally and communicate with the FastAPI backend running on `localhost`.

**Acceptance Criteria:**
1.  Set up the basic Vite + React project structure.
2.  Implement core routing for the main views: Dashboard, Habits, Journaling.
3.  Develop a consistent UI shell using Tailwind CSS (header, sidebar navigation).
4.  Implement a global API service layer (e.g., Axios wrapper) to handle HTTP requests to `http://localhost:port/api/v1`.

**Labels:** frontend, task

---

## [BACKEND] Implement Local LLM Processing API Endpoint

**Labels:** backend,advanced,task

### Goal: Implement the local LLM processing endpoint.

This task integrates the advanced, zero-cost AI feature using `llama-cpp-python`. It must run entirely locally and not rely on external APIs.

**Acceptance Criteria:**
1.  Create the `POST /api/v1/llm/process` endpoint in FastAPI.
2.  The endpoint must accept `{prompt: string, text_content: string}`.
3.  Implement the local model loading and inference logic using `llama-cpp-python`.
4.  Return a structured JSON response containing the processed text (e.g., summary or analysis).

**Labels:** backend, advanced, task

---

## [CRITICAL] Test Suite Fails Due to pydantic-core Dependency Build Error

**Labels:** bug,environment,testing

**Environment Failure:** The test suite fails during dependency installation/wheel building for `pydantic-core`. This is a critical setup error that prevents any functional testing of the API endpoints, as the FastAPI application cannot be reliably initialized within the isolated virtual environment.

**Error Trace Snippet:**
```
TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'
...
ERROR: Failed building wheel for pydantic-core
```

**Steps to Reproduce:**
1. Run `run_tests`.
2. The process fails during the installation of dependencies, specifically when compiling `pydantic-core`.

**Actual Result:** Test run terminates with a dependency build failure (`exit status: 101`).
**Expected Result:** All tests in `tests/test_api.py` execute successfully, confirming the core functionality of Habit Management, Logging, and Journaling endpoints.

---

## [API] Implement Habit Analytics/Stats Endpoint

**Labels:** backend,task

**Due:** 2026-08-07

**Context:** We need a core utility function/module in the backend that calculates simple metrics (e.g., streak, total completion count) based on the `HabitLogs` table data. This will be necessary for any dashboard view.
*   **Goal:** Create a helper service/function exposed via FastAPI endpoint (e.g., `/api/v1/habits/{habit_id}/stats`) that accepts a date range and calculates:
    1.  Current Streak (Consecutive days of completion).
    2.  Total Completion Rate (Completed logs / Total dates checked).
*   **Input:** `habit_id`, `start_date`, `end_date`.
*   **Output:** Structured JSON summary for these metrics.

---

## [INFRA] Set up FastAPI Boilerplate & SQLite Connection

**Labels:** backend,task

**Due:** 2026-08-03

**Context:** This task is the foundational infrastructure for the entire application. We must set up a barebones FastAPI server running in local development mode that can connect to an SQLite database file (`app.db`).
*   **Goal:** Initialize project structure and define basic DB connection logic (e.g., using SQLAlchemy or similar pattern).
*   **Deliverable:** A minimal `main.py` accessible endpoint (e.g., `/health`) that confirms the backend is running and successfully connected to the local SQLite instance without throwing errors.

Please ensure all code remains clean, modular, and adheres to FastAPI best practices. Focus only on structure and connectivity for now.

---

