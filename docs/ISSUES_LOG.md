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

