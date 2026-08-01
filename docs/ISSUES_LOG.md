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

