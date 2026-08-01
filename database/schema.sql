-- --------------------------------------------------------------
-- SQLite Schema Definition for Local Habit Tracker Data Store
-- Purpose: Stores all user habit definitions and daily progress records.
-- Optimization Note: Indexes are added to ensure efficient date range queries,
-- which are necessary for streak calculation (the primary usage pattern).
-- --------------------------------------------------------------

-- Table 1: users
-- Minimal user table. Since the app is designed for local, single-instance use,
-- this tracks basic identity data.
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    device_info TEXT
);

-- Table 2: habits
-- Defines the specific habits the user wants to track.
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    target_value REAL DEFAULT 0.0, -- Target unit value (e.g., 30 minutes)
    unit TEXT NOT NULL DEFAULT 'times', -- e.g., "minutes", "reps", "times"
    is_active BOOLEAN DEFAULT TRUE,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,

    -- Foreign Key Constraint: Links habits to a user
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,

    UNIQUE(user_id, name)
);

CREATE INDEX IF NOT EXISTS idx_habits_user_id ON habits (user_id);


-- Table 3: daily_entries
-- The core time-series tracking table. One entry per habit, per day.
CREATE TABLE IF NOT EXISTS daily_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER NOT NULL,

    -- Use TEXT format 'YYYY-MM-DD' for standardized date storage and querying.
    entry_date TEXT NOT NULL, 

    value_recorded REAL DEFAULT 0.0, -- The actual value achieved that day
    completed BOOLEAN DEFAULT FALSE,  -- Quick check: Was the habit tracked/attempted?

    FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE,

    -- Composite Unique Index is CRITICAL: Ensures only one record exists per Habit/Date pair.
    UNIQUE (habit_id, entry_date) 
);


-- Create an index optimized for streak checking and date range queries.
CREATE INDEX IF NOT EXISTS idx_daily_entries_lookup ON daily_entries (habit_id, entry_date);