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

## [API] Implement Habit CRUD Operations (POST/GET)

**Labels:** backend,task

**Due:** 2026-08-05

**Context:** Now that the `Habits` table exists, we must implement the full CRUD operations for creating and retrieving habits.
*   **API Endpoint:** `POST /api/v1/habits` (Create a new habit)
    *   *Payload:* `{name: string, description: string}`
    *   *Expected Behavior:* Inserts into the `Habits` table and returns the newly created Habit object.
*   **API Endpoint:** `GET /api/v1/habits` (List all active habits)
    *   *Payload:* None.
    *   *Expected Behavior:* Queries the entire `Habits` table and returns an array of habit objects.

Focus on robust input validation within FastAPI using Pydantic models.

---

## [DB] Implement Initial Database Schema Migration Script

**Labels:** backend,task

**Due:** 2026-08-04

**Context:** Using the established database connection from the infrastructure setup task, we need to implement the initialization script for the core data model.
*   **Goal:** Write and run a function/script that checks if the necessary tables exist in the SQLite DB and creates them if they do not (Idempotent schema migration).
*   **Required Tables (based on ARCHITECTURE.md):**
    1.  `Habits`: (`habit_id`, `name`, `description`, `creation_date`, `is_active`)
    2.  `HabitLogs`: (`log_id`, `habit_id`, `date`, `is_completed`, `value`)
    3.  `JournalEntries`: (`entry_id`, `user_id`, `date`, `content`, `related_habit_id`)

This script should be callable early in the backend startup process to ensure data readiness.

---

## [UI] Implement Basic Habit List View & Creator Form

**Labels:** frontend,task

**Due:** 2026-08-05

**Context:** The frontend needs a basic view to display and manage habits. This component should only consume the endpoints defined in [API] Implement Habit CRUD Operations (Issue #X).
*   **Goal:** Create a main `HabitList` component that fetches all habits on load (`GET /api/v1/habits`) and provides an input form to create new ones (`POST /api/v1/habits`).
*   **Tech Stack:** React, Tailwind CSS, vanilla JS.
*   **Assumption:** The backend endpoints are stable by the time this task starts (i.e., Issue #3 is complete).

---

## [Phase 1] Implement Habit Log Logging and History Retrieval (API v1/logs)

**Labels:** backend,task

**Due:** 2024-07-26

The most critical endpoint is logging daily progress. This task defines the full lifecycle of recording a habit's completion status or metric for a specific date.

**Contract Definition:**
*   **POST /api/v1/logs**: Log progress. *Request:* `{habit_id: int, date: str (YYYY-MM-DD), is_completed: bool, value: float | null}`. The endpoint must enforce the unique constraint on (`habit_id`, `date`).
*   **GET /api/v1/logs/history**: Retrieve all historical logs for a given habit and date range. *Params:* `?habit_id={id}&start_date={date1}&end_date={date2}`. *Response:* Array of `{log_id: int, date: str, is_completed: bool, value: float | null}`.

**Implementation Focus:** Implement the transaction logic to handle creation and complex filtering for historical views. Must return proper error handling (e.g., 400 if dates are invalid or IDs don't exist).

---

## [Phase 0] Implement Habit CRUD Endpoints (API v1/habits)

**Labels:** backend,task

**Due:** 2024-07-19

The FastAPI backend needs a robust implementation for managing user habits (parent entity). This includes creating, retrieving all active habits, and updating habit details.

**Contract Definition:**
*   **GET /api/v1/habits**: List all active Habit objects. *Response:* `[{habit_id: int, name: str, description: str, is_active: bool}]`
*   **POST /api/v1/habits**: Create a new habit. *Request:* `{name: str, description: str}`. *Success:* Returns the newly created object including its `habit_id`.
*   **PUT /api/v1/habits/{habit_id}**: Update existing habit details. *Path:* Requires `habit_id`. *Request:* `{name?: str, description?: str}`.

**Implementation Focus:** Use Pydantic models for strict request and response validation. Ensure all operations interact correctly with the `Habits` table in SQLite.

---

## [Phase 2] Implement Journal Entry CRUD Endpoints (API v1/journal)

**Labels:** backend,task

**Due:** 2024-08-02

This feature handles reflective journaling entries. It must be decoupled from specific habits but linked to a date for contextual retrieval.

**Contract Definition:**
*   **POST /api/v1/journal**: Create a new journal entry. *Request:* `{date: str (YYYY-MM-DD), content: str, related_habit_id?: int | null}`. The `related_habit_id` must be optional and handle the case where it's null (general reflection).
*   **GET /api/v1/journal**: Retrieve all entries for a specific date. *Params:* `?date={date}`. *Response:* Array of `{entry_id: int, date: str, content: str, related_habit_id?: int | null}`.

**Implementation Focus:** Ensure data validation on the required `date` and `content`. This endpoint is essential for generating historical reports/summaries later.

---

## [Phase 3] Integration Testing & API Contract Finalization (End-to-End Test Plan)

**Labels:** backend,frontend,task

**Due:** 2024-08-09

The final tasks involve ensuring the full contract is tested and that the front end can consume the data effectively.

**Backend Task:**
*   Implement API documentation endpoints (`/api/v3/docs`) to verify all paths are correctly defined with schema validation (Swagger/Redoc generation).

**Frontend Consumption task for UI Team:**
*   Create mock services or dedicated dummy component screens that *consume* the final API contracts defined above. This allows the UI team to proceed with visual layout and state management while backend tasks are finalized, minimizing integration waiting time.

This ticket acts as a coordination point and acceptance check before considering the system 'complete' for V1 release.

---

## [Phase 0] Implement Habit CRUD Endpoints (API v1/habits)

**Labels:** backend,task

**Due:** 2024-07-19

The FastAPI backend needs a robust implementation for managing user habits (parent entity). This includes creating, retrieving all active habits, and updating habit details.

**Contract Definition:**
*   **GET /api/v1/habits**: List all active Habit objects. *Response:* `[{habit_id: int, name: str, description: str, is_active: bool}]`
*   **POST /api/v1/habits**: Create a new habit. *Request:* `{name: str, description: str}`. *Success:* Returns the newly created object including its `habit_id`.
*   **PUT /api/v1/habits/{habit_id}**: Update existing habit details. *Path:* Requires `habit_id`. *Request:* `{name?: str, description?: str}`.

**Implementation Focus:** Use Pydantic models for strict request and response validation. Ensure all operations interact correctly with the `Habits` table in SQLite.

---

## [Phase 2] Implement Journal Entry CRUD Endpoints (API v1/journal)

**Labels:** backend,task

**Due:** 2024-08-02

This feature handles reflective journaling entries. It must be decoupled from specific habits but linked to a date for contextual retrieval.

**Contract Definition:**
*   **POST /api/v1/journal**: Create a new journal entry. *Request:* `{date: str (YYYY-MM-DD), content: str, related_habit_id?: int | null}`. The `related_habit_id` must be optional and handle the case where it's null (general reflection).
*   **GET /api/v1/journal**: Retrieve all entries for a specific date. *Params:* `?date={date}`. *Response:* Array of `{entry_id: int, date: str, content: str, related_habit_id?: int | null}`.

**Implementation Focus:** Ensure data validation on the required `date` and `content`. This endpoint is essential for generating historical reports/summaries later.

---

## [Phase 1] Implement Habit Log Logging and History Retrieval (API v1/logs)

**Labels:** backend,task

**Due:** 2024-07-26

The most critical endpoint is logging daily progress. This task defines the full lifecycle of recording a habit's completion status or metric for a specific date.

**Contract Definition:**
*   **POST /api/v1/logs**: Log progress. *Request:* `{habit_id: int, date: str (YYYY-MM-DD), is_completed: bool, value: float | null}`. The endpoint must enforce the unique constraint on (`habit_id`, `date`).
*   **GET /api/v1/logs/history**: Retrieve all historical logs for a given habit and date range. *Params:* `?habit_id={id}&start_date={date1}&end_date={date2}`. *Response:* Array of `{log_id: int, date: str, is_completed: bool, value: float | null}`.

**Implementation Focus:** Implement the transaction logic to handle creation and complex filtering for historical views. Must return proper error handling (e.g., 400 if dates are invalid or IDs don't exist).

---

