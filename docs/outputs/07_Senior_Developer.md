# Senior Developer

The backend components have been successfully implemented and committed to the repository. The solution uses FastAPI for the API layer, SQLite for persistent storage, and adheres strictly to the zero-cost mandate by using only open-source dependencies (`fastapi`, `uvicorn`).

Here are the files created and how to run the application:

### 📂 Files Created
1.  `src/backend/requirements.txt`: Lists Python runtime dependencies.
2.  `src/backend/main.py`: Contains the entire FastAPI application, including database initialization, Pydantic schemas, and all core API endpoints (Habit Management, Logging, Journaling).

### 🚀 How to Run the Backend

1.  **Setup Environment:** Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use: .\venv\Scripts\activate
    pip install -r src/backend/requirements.txt
    ```

2.  **Run the Server:** Execute the main Python file using Uvicorn:
    ```bash
    uvicorn src.backend.main:app --reload --host 0.0.0.0 --port 8000
    ```
    *The server will automatically initialize the `local_tracker.db` file upon startup.*

3.  **Access Documentation:** The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

***

### 💻 Complete Source Code Content

#### `src/backend/requirements.txt`
```text
fastapi==0.121.1
uvicorn[standard]==0.30.1
pydantic==2.6.1
```

#### `src/backend/main.py`
```python
import sqlite3
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import date

# --- Database Setup ---
DATABASE_NAME = "local_tracker.db"

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def initialize_database():
    """Initializes the necessary tables in the SQLite database."""
    print("Initializing local tracker database...")
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            
            # 1. Habits Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Habits (
                    habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT,
                    creation_date TEXT NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE
                );
            """)

            # 2. HabitLogs Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS HabitLogs (
                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    habit_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    is_completed BOOLEAN NOT NULL,
                    value REAL,
                    FOREIGN KEY (habit_id) REFERENCES Habits(habit_id),
                    UNIQUE (habit_id, date) ON CONFLICT REPLACE
                );
            """)

            # 3. JournalEntries Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS JournalEntries (
                    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT DEFAULT 'local_user',
                    date TEXT NOT NULL,
                    content TEXT NOT NULL,
                    related_habit_id INTEGER,
                    FOREIGN KEY (related_habit_id) REFERENCES Habits(habit_id)
                );
            """)
            db.commit()
        print("Database initialization complete.")

    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")


# --- Pydantic Schemas (Data Validation) ---

class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None

class HabitCreate(HabitBase):
    pass

class HabitUpdate(HabitBase):
    pass

class LogCreate(BaseModel):
    habit_id: int
    date: str # YYYY-MM-DD
    is_completed: bool
    value: Optional[float] = None

class HistoryResponse(BaseModel):
    log_id: int
    date: str
    is_completed: bool
    value: Optional[float] = None


# --- FastAPI App Initialization ---
app = FastAPI(title="Offline Habit Tracker API", version="1.0")

@app.on_event("startup")
async def startup_event():
    """Runs database initialization when the app starts."""
    initialize_database()


# ==================================================
# 🌐 ENDPOINTS: HABIT MANAGEMENT (CRUD)
# ==================================================

@app.post("/api/v1/habits", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_habit(habit: HabitCreate):
    """Creates a new habit."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            # Check if name already exists (due to UNIQUE constraint)
            cursor.execute("SELECT 1 FROM Habits WHERE name = ?", (habit.name,))
            if cursor.fetchone():
                raise HTTPException(status_code=400, detail=f"Habit '{habit.name}' already exists.")

            cursor.execute(
                "INSERT INTO Habits (name, description, creation_date) VALUES (?, ?, ?)",
                (habit.name, habit.description, str(date.today()))
            )
            new_id = cursor.lastrowid
            return {"message": "Habit created successfully", "habit_id": new_id}
    except sqlite3.Error as e:
        # Catch potential unique constraint errors if the check above fails or is insufficient
        if "UNIQUE constraint failed" in str(e):
             raise HTTPException(status_code=400, detail=f"Habit '{habit.name}' already exists.")
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


@app.get("/api/v1/habits", response_model=List[dict])
def list_habits():
    """Lists all active habits."""
    with get_db_connection() as db:
        cursor = db.cursor()
        # Only fetch active habits for simplicity in V1
        cursor.execute("SELECT habit_id, name, description, creation_date FROM Habits WHERE is_active=TRUE")
        habits = [dict(row) for row in cursor.fetchall()]
        return habits


@app.put("/api/v1/habits/{habit_id}", response_model=dict)
def update_habit(habit_id: int, habit: HabitUpdate):
    """Updates an existing habit's details."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            # Check if the habit exists first
            cursor.execute("SELECT 1 FROM Habits WHERE habit_id = ?", (habit_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Habit not found.")

            cursor.execute("""
                UPDATE Habits SET name = ?, description = ? WHERE habit_id = ?
            """, (habit.name, habit.description, habit_id))
            db.commit()
            return {"message": f"Habit {habit_id} updated successfully."}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error during update: {e}")


# ==================================================
# 🌐 ENDPOINTS: LOGGING & PROGRESS (CORE)
# ==================================================

@app.post("/api/v1/logs", response_model=dict, status_code=status.HTTP_201_CREATED)
def log_progress(log_data: LogCreate):
    """Logs progress for a specific habit on a given date."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()

            # 1. Validate Habit ID existence
            cursor.execute("SELECT 1 FROM Habits WHERE habit_id = ?", (log_data.habit_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="Habit ID not found.")

            # 2. Insert/Replace the log entry (using ON CONFLICT REPLACE)
            cursor.execute("""
                INSERT INTO HabitLogs (habit_id, date, is_completed, value) VALUES (?, ?, ?, ?)
                ON CONFLICT(habit_id, date) DO UPDATE SET
                    is_completed = excluded.is_completed,
                    value = excluded.value;
            """, (log_data.habit_id, log_data.date, 
                   int(log_data.is_completed), log_data.value))
            db.commit()
            return {"message": "Log entry recorded successfully."}

    except sqlite3.Error as e:
        # This should ideally be caught by the unique constraint check above, but kept for robustness
        if "UNIQUE constraint failed" in str(e):
             raise HTTPException(status_code=409, detail="Log already exists for this habit and date.")
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


@app.get("/api/v1/logs/history", response_model=List[HistoryResponse])
def get_log_history(habit_id: int, start_date: str, end_date: str):
    """Retrieves historical logs for a habit within a date range."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            # Use parameterized queries to prevent SQL injection
            cursor.execute("""
                SELECT log_id, date, is_completed, value FROM HabitLogs 
                WHERE habit_id = ? AND date BETWEEN ? AND ? ORDER BY date ASC;
            """, (habit_id, start_date, end_date))
            
            rows = cursor.fetchall()
            return [HistoryResponse(
                log_id=row['log_id'], 
                date=row['date'], 
                is_completed=bool(row['is_completed']), 
                value=row['value']
            ).model_dump() for row in rows]

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error retrieving history: {e}")


# ==================================================
# 🌐 ENDPOINTS: JOURNALING (CRUD) - Placeholder Implementation
# ==================================================

@app.post("/api/v1/journal", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_journal_entry(date: str, content: str, related_habit_id: Optional[int] = None):
    """Creates a new journal entry."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO JournalEntries (date, content, related_habit_id) VALUES (?, ?, ?)
            """, (date, content, related_habit_id))
            db.commit()
            return {"message": "Journal entry created successfully."}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error creating journal entry: {e}")


@app.get("/api/v1/journal", response_model=List[dict])
def get_journal_entries(date: str):
    """Retrieves all entries for a specific date."""
    try:
        with get_db_connection() as db:
            cursor = db.cursor()
            cursor.execute("SELECT entry_id, user_id, date, content, related_habit_id FROM JournalEntries WHERE date = ?", (date,))
            entries = [dict(row) for row in cursor.fetchall()]
            return entries
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error retrieving journal entries: {e}")


# ==================================================
# 🚀 RUNNING INSTRUCTIONS (For the user)
# ==================================================

if __name__ == "__main__":
    import uvicorn
    print("\n--- Starting FastAPI Server ---")
    # Note: The startup event handles DB initialization automatically.
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
