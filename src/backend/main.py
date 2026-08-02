from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import os

# Configuration
DATA_DIR = os.getenv("DATA_DIR", "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DB_PATH = f"sqlite:///{os.path.join(DATA_DIR, 'game.db')}"

app = FastAPI()

# Database setup (simple sqlite3 integration)
def init_db():
    conn = sqlite3.connect(os.path.join(DATA_DIR, "game.db"))
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS high_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class ScoreSubmission(BaseModel):
    player_name: str
    score: int

@app.get("/scores")
async def get_scores():
    conn = sqlite3.connect(os.path.join(DATA_DIR, "game.db"))
    cursor = conn.cursor()
    cursor.execute("SELECT player_name, score FROM high_scores ORDER BY score DESC LIMIT 10")
    results = cursor.fetchall()
    conn.close()
    return [{"player_name": r[0], "score": r[1]} for r in results]

@app.post("/submit-score")
async def submit_score(submission: ScoreSubmission):
    conn = sqlite3.connect(os.path.join(DATA_DIR, "game.db"))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO high_scores (player_name, score) VALUES (?, ?)", 
                    (submission.player_name, submission.score))
    conn.commit()
    conn.close()
    return {"message": "Score submitted"}
