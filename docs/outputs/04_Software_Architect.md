# Software Architect

The system architecture has been designed and committed to `ARCHITECTURE.md` following the absolute zero-cost mandate.

Here is the component list as requested:

### 🧩 Components & Technology Stack
The system is designed as a tightly coupled, client-server architecture running entirely locally on the user's device.

1.  **Frontend (Client): React + Vite + Tailwind CSS**
    *   **Role:** Provides the User Interface and handles all local rendering logic. It communicates solely with the Backend API via HTTP requests.
    *   **Constraint:** Must be a single-page application (SPA) that runs locally.
2.  **Backend (Server): FastAPI (Python)**
    *   **Role:** Acts as the primary business logic layer and data access interface. It receives requests from the Frontend, validates them, interacts with the Database, and returns structured JSON responses.
    *   **Constraint:** Must be containerized or packaged for local execution (e.g., using a simple Python executable wrapper).
3.  **Database: SQLite (`sqlite3` module)**
    *   **Role:** The single source of truth for all user data. It is file-based, ensuring maximum data sovereignty and zero external server dependencies.
    *   **Constraint:** Data never leaves the local device filesystem.
4.  **Advanced Feature (Optional): Local LLM Runtime (`llama-cpp-python`)**
    *   **Role:** Provides advanced text processing capabilities (e.g., summarizing journal entries, classifying mood). It runs entirely in memory on the user's CPU/GPU and requires no external API calls.
    *   **Constraint:** Used only for local computation; never for data transmission or retrieval from external services.

***

### ARCHITECTURE.md Content:

```markdown
## 🏗️ System Architecture Design - Offline Habit Tracker

*Mandate Adherence: Absolute Zero Operational Expenditure (OpEx). All components are free and self-hostable/local.* 
*Source Strategy: Based on TECH_STRATEGY.md.*

---

### 🧩 Components & Technology Stack
The system is designed as a tightly coupled, client-server architecture running entirely locally on the user's device.

1.  **Frontend (Client): React + Vite + Tailwind CSS**
    *   **Role:** Provides the User Interface and handles all local rendering logic. It communicates solely with the Backend API via HTTP requests.
    *   **Constraint:** Must be a single-page application (SPA) that runs locally.
2.  **Backend (Server): FastAPI (Python)**
    *   **Role:** Acts as the primary business logic layer and data access interface. It receives requests from the Frontend, validates them, interacts with the Database, and returns structured JSON responses.
    *   **Constraint:** Must be containerized or packaged for local execution (e.g., using a simple Python executable wrapper).
3.  **Database: SQLite (`sqlite3` module)**
    *   **Role:** The single source of truth for all user data. It is file-based, ensuring maximum data sovereignty and zero external server dependencies.
    *   **Constraint:** Data never leaves the local device filesystem.
4.  **Advanced Feature (Optional): Local LLM Runtime (`llama-cpp-python`)**
    *   **Role:** Provides advanced text processing capabilities (e.g., summarizing journal entries, classifying mood). It runs entirely in memory on the user's CPU/GPU and requires no external API calls.
    *   **Constraint:** Used only for local computation; never for data transmission or retrieval from external services.

---

### 💾 Data Model (SQLite Schema)
The core database schema is designed around tracking habits, logging daily progress, and journaling reflections.

**1. `Habits` Table**
*   **Purpose:** Defines the user's goals/habits.
*   **Fields:**
    *   `habit_id`: INTEGER PRIMARY KEY (Unique identifier)
    *   `name`: TEXT NOT NULL (e.g., 'Read 30 mins', 'Meditate')
    *   `description`: TEXT (Detailed goal description)
    *   `creation_date`: TEXT (ISO format: YYYY-MM-DD)
    *   `is_active`: BOOLEAN (Whether the habit is currently tracked)

**2. `HabitLogs` Table**
*   **Purpose:** Records the daily completion status for a specific habit.
*   **Fields:**
    *   `log_id`: INTEGER PRIMARY KEY
    *   `habit_id`: INTEGER NOT NULL (FOREIGN KEY to `Habits`) 
    *   `date`: TEXT NOT NULL (Date of logging, YYYY-MM-DD)
    *   `is_completed`: BOOLEAN (True if goal was met)
    *   `value`: REAL (Optional metric/quantity logged, e.g., minutes read)
    *   **Constraint:** Unique constraint on (`habit_id`, `date`) to prevent duplicate entries.

**3. `JournalEntries` Table**
*   **Purpose:** Stores reflective thoughts linked to a date or habit.
*   **Fields:**
    *   `entry_id`: INTEGER PRIMARY KEY
    *   `user_id`: TEXT (Placeholder for future user context, currently simple)
    *   `date`: TEXT NOT NULL (Date of entry, YYYY-MM-DD)
    *   `content`: TEXT (The main journal text)
    *   `related_habit_id`: INTEGER (FOREIGN KEY to `Habits`, nullable if general reflection)

---

### 🌐 API Surface (FastAPI Endpoints)
All endpoints are local and communicate with the SQLite database.

**1. Habit Management (`/api/v1/habits`)**
*   `POST /`: Create a new habit. (Body: `{name, description}`) 
    *   *Returns:* New `habit_id`.
*   `GET /`: List all active habits. 
    *   *Params:* None.
    *   *Returns:* Array of Habit objects.
*   `PUT /{habit_id}`: Update habit details (e.g., name, description).
    *   *Params:* `habit_id` in path.

**2. Logging & Progress (`/api/v1/logs`)**
*   `POST /`: Log progress for a specific date and habit. 
    *   *Body:* `{habit_id, date, is_completed, value}`.
    *   *Returns:* Confirmation of log creation.
*   `GET /history?habit_id={id}&start_date={date1}&end_date={date2}`: Retrieve historical logs for a habit. 
    *   *Returns:* Array of `HabitLogs` objects (including streak calculation data).

**3. Journaling (`/api/v1/journal`)**
*   `POST /`: Create a new journal entry. 
    *   *Body:* `{date, content, related_habit_id}`.
*   `GET /?date={date}`: Retrieve all entries for a specific date.
    *   *Returns:* Array of JournalEntry objects.

**4. LLM Processing (`/api/v1/llm/process`)** (Advanced)
*   `POST /`: Sends text content to the local LLM model for processing. 
    *   *Body:* `{prompt: "Summarize this journal entry:", text_content: "..."}`.
    *   *Returns:* `{processed_text: "..."}` (The summary/analysis).

---

### 🔄 Request Flow Example: Logging a Habit Completion

1.  **User Action:** User opens the app and taps 'Complete' for 'Meditate' on today's date.
2.  **Frontend:** React component captures the action, constructs the payload (`{habit_id: 5, date: "2024-06-28", is_completed: true, value: null}`), and sends a `POST` request to `/api/v1/logs`.
3.  **Backend (FastAPI):** The FastAPI endpoint receives the request. It performs validation (e.g., checking if `habit_id` exists).
4.  **Database Interaction:** FastAPI executes an SQL INSERT statement against the SQLite file: `INSERT INTO HabitLogs (habit_id, date, is_completed, value) VALUES (?, ?, ?, ?)`.
5.  **Response:** The database confirms success. FastAPI returns a HTTP 201 Created status and a confirmation JSON payload to the Frontend.
6.  **Frontend Update:** React receives the success response and updates the local UI state (e.g., marking the habit as completed for today).

---

### 🚀 Deployment Strategy (Zero Cost)
The entire application must be packaged into a single, self-contained unit to guarantee offline functionality.

1.  **Packaging Tool:** Use a framework like **Electron** or Python's **PyInstaller** (if focusing purely on the backend executable) to bundle the necessary components.
2.  **Structure:** The final package must contain:
    *   The JavaScript/HTML assets (React build).
    *   The Python runtime environment and FastAPI code.
    *   The SQLite database schema initialization script.
3.  **Execution Flow:** Upon launch, the wrapper executes the backend server first (`uvicorn` or similar local runner), which initializes the SQLite file. The React frontend then loads and makes API calls to `localhost:port`, ensuring all services run within the same process space or locally accessible network namespace.
```
