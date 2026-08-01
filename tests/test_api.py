import pytest
from fastapi.testclient import TestClient
from datetime import date
import sqlite3
import os

# Import the FastAPI app and database setup from the main module
from src.backend.main import app, get_db_connection, initialize_database, DATABASE_NAME

# --- Setup/Teardown Fixtures ---

@pytest.fixture(scope="session", autouse=True)
def cleanup_db():
    """Fixture to ensure a clean database state before running tests."""
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
    # Initialize the DB structure once for all tests in this session
    initialize_database()

@pytest.fixture(scope="function")
def client():
    """Pytest fixture to provide a TestClient instance."""
    # The app is already configured with the database connection via startup event
    with TestClient(app) as c:
        yield c

def get_db_connection_for_test():
    """Helper function to get a fresh DB connection for manual checks if needed."""
    return get_db_connection()


# --- Test Cases ---

class TestHabitManagement:
    @pytest.fixture(autouse=True)
    def setup_habits(self, client):
        """Setup initial habits before running habit tests."""
        with client.client.app.dependency_overrides.get("get_db_connection"):
            # Override the connection getter to ensure we use a fresh context for setup if needed, 
            # but since cleanup_db runs first, direct calls should be fine.
            pass

    def test_create_habit_success(self, client):
        """Tests successful creation of a new habit."""
        new_habit = {"name": "Read Book", "description": "30 minutes daily"}
        response = client.post("/api/v1/habits", json=new_habit)
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Habit created successfully"
        assert "habit_id" in data

    def test_create_habit_already_exists(self, client):
        """Tests failure when creating a habit with an existing name."""
        # 1. Create the habit once
        initial_habit = {"name": "Meditate", "description": "Daily calm"}
        client.post("/api/v1/habits", json=initial_habit)

        # 2. Attempt to create it again
        response = client.post("/api/v1/habits", json=initial_habit)
        assert response.status_code == 400
        data = response.json()
        assert "Habit 'Meditate' already exists." in data["detail"]

    def test_list_all_habits(self, client):
        """Tests listing all active habits."""
        # Setup two distinct habits
        client.post("/api/v1/habits", json={"name": "Run 5k", "description": None})
        client.post("/api/v1/habits", json={"name": "Drink Water", "description": "2L"})

        response = client.get("/api/v1/habits")
        assert response.status_code == 200
        data = response.json()
        # We expect at least the two habits we created
        assert len(data) >= 2
        
    def test_update_habit_success(self, client):
        """Tests successful update of an existing habit."""
        # Setup initial habit
        initial_habit = {"name": "Old Name", "description": "Old description"}
        response = client.post("/api/v1/habits", json=initial_habit)
        habit_id = response.json()["habit_id"]

        # Update the habit
        update_data = {"name": "New Habit Name", "description": "Updated goal"}
        response = client.put(f"/api/v1/habits/{habit_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == f"Habit {habit_id} updated successfully."

    def test_update_nonexistent_habit(self, client):
        """Tests failure when updating a non-existent habit."""
        response = client.put("/api/v1/habits/999", json={"name": "Ghost", "description": None})
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Habit not found."


class TestLoggingAndHistory:
    @pytest.fixture(autouse=True)
    def setup_habits_and_logs(self, client):
        """Setup a consistent habit for logging tests."""
        # Create a specific habit ID to use across log tests
        habit = {"name": "Test Habit", "description": None}
        client.post("/api/v1/habits", json=habit)
        
        # Get the ID of the created habit (assuming it's the first one and exists)
        response = client.get("/api/v1/habits")
        habits = response.json()
        self.test_habit_id = habits[0]["habit_id"]

    def test_log_progress_success(self, client):
        """Tests successful logging of progress."""
        # Log completion for today
        today_date = date.today().strftime("%Y-%m-%d")
        log_data = {
            "habit_id": self.test_habit_id,
            "date": today_date,
            "is_completed": True,
            "value": 45.5
        }
        response = client.post("/api/v1/logs", json=log_data)
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Log entry recorded successfully."

    def test_log_progress_conflict_update(self, client):
        """Tests updating an existing log entry (conflict resolution)."""
        # 1. Initial log (incomplete)
        today_date = date.today().strftime("%Y-%m-%d")
        initial_data = {
            "habit_id": self.test_habit_id,
            "date": today_date,
            "is_completed": False,
            "value": 10.0
        }
        client.post("/api/v1/logs", json=initial_data)

        # Wait a moment to ensure the DB transaction completes (though usually unnecessary in test client)
        import time; time.sleep(0.1) 

        # 2. Update log (complete, new value)
        update_data = {
            "habit_id": self.test_habit_id,
            "date": today_date,
            "is_completed": True, # Changed status
            "value": 90.5 # Changed value
        }
        response = client.post("/api/v1/logs", json=update_data)
        assert response.status_code == 201
        # The API uses ON CONFLICT REPLACE, so it should succeed and overwrite the data

    def test_log_progress_habit_not_found(self, client):
        """Tests failure when logging progress for a non-existent habit ID."""
        non_existent_id = 9999
        log_data = {
            "habit_id": non_existent_id,
            "date": date.today().strftime("%Y-%m-%d"),
            "is_completed": True,
            "value": None
        }
        response = client.post("/api/v1/logs", json=log_data)
        assert response.status_code == 404
        data = response.json()
        assert "Habit ID not found." in data["detail"]

    def test_get_history_success(self, client):
        """Tests retrieving historical logs for a habit."""
        # Setup: Log entries for three different dates
        today_date = date.today().strftime("%Y-%m-%d")
        yesterday_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        last_week_date = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")

        # Log 1: Today, Completed, Value 50
        client.post("/api/v1/logs", json={"habit_id": self.test_habit_id, "date": today_date, "is_completed": True, "value": 50})
        # Log 2: Yesterday, Incomplete, No Value
        client.post("/api/v1/logs", json={"habit_id": self.test_habit_id, "date": yesterday_date, "is_completed": False, "value": None})
        # Log 3: Last Week, Completed, Value 20
        client.post("/api/v1/logs", json={"habit_id": self.test_habit_id, "date": last_week_date, "is_completed": True, "value": 20})

        # Test retrieval for a range covering all three dates
        start_date = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")
        end_date = date.today().strftime("%Y-%m-%d")

        response = client.get(f"/api/v1/logs/history?habit_id={self.test_habit_id}&start_date={start_date}&end_date={end_date}")
        assert response.status_code == 200
        data = response.json()
        # We expect exactly 3 logs
        assert len(data) == 3

    def test_get_history_no_results(self, client):
        """Tests history retrieval when no logs exist in the range."""
        # Use a date range far in the future where we haven't logged anything
        future_start = (date.today() + timedelta(days=10)).strftime("%Y-%m-%d")
        future_end = (date.today() + timedelta(days=15)).strftime("%Y-%m-%d")

        response = client.get(f"/api/v1/logs/history?habit_id={self.test_habit_id}&start_date={future_start}&end_date={future_end}")
        assert response.status_code == 200
        data = response.json()
        # Expect an empty list
        assert len(data) == 0


class TestJournaling:
    @pytest.fixture(autouse=True)
    def setup_habits(self, client):
        """Setup a habit for journaling tests."""
        habit = {"name": "Test Habit", "description": None}
        client.post("/api/v1/habits", json=habit)
        response = client.get("/api/v1/habits")
        self.test_habit_id = response.json()[0]["habit_id"]

    def test_create_journal_entry_with_related_habit(self, client):
        """Tests creating a journal entry linked to a habit."""
        date_str = date.today().strftime("%Y-%m-%d")
        content = "Had a productive day focusing on my goals."
        response = client.post("/api/v1/journal", json={"date": date_str, "content": content, "related_habit_id": self.test_habit_id})
        assert response.status_code == 201
        data = response.json()
        assert data["message"] == "Journal entry created successfully."

    def test_create_journal_entry_general(self, client):
        """Tests creating a general journal entry (no related habit)."""
        date_str = date.today().strftime("%Y-%m-%d")
        content = "Just thinking about the week ahead."
        response = client.post("/api/v1/journal", json={"date": date_str, "content": content})
        assert response.status_code == 201

    def test_get_journal_entries_success(self, client):
        """Tests retrieving journal entries for a specific date."""
        # Setup: Create two entries for the same day
        date_str = date.today().strftime("%Y-%m-%d")
        client.post("/api/v1/journal", json={"date": date_str, "content": "Entry 1"})
        client.post("/api/v1/journal", json={"date": date_str, "content": "Entry 2 (Habit related)", "related_habit_id": 1})

        # Retrieve entries
        response = client.get(f"/api/v1/journal?date={date_str}")
        assert response.status_code == 200
        data = response.json()
        # Expect two entries
        assert len(data) == 2

    def test_get_journal_entries_no_results(self, client):
        """Tests retrieving journal entries for a date with no records."""
        future_date = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")
        response = client.get(f"/api/v1/journal?date={future_date}")
        assert response.status_code == 200
        data = response.json()
        # Expect an empty list
        assert len(data) == 0

# Required imports for date arithmetic in tests
from datetime import timedelta