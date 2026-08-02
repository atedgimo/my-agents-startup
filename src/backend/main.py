from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import os

# Configuration
DATA_DIR = os.getenv("DATA_DIR", "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

app = FastAPI()

# Serve frontend static files from src directory
app.mount("/static", StaticFiles(directory="../src"), name="static")

@app.get("/")
async def root():
    return FileResponse("../src/index.html")

# Database setup
DB_PATH = os.path.join(DATA_DIR, "game.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT player_name, score FROM high_scores ORDER BY score DESC LIMIT 10")
    results = cursor.fetchall()
    conn.close()
    return [{"player_name": r[0], "score": r[1]} for r in results]

@app.post("/submit-score")
async def submit_score(submission: ScoreSubmission):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO high_scores (player_name, score) VALUES (?, ?)", 
                   (submission.player_name, submission.score))
    conn.commit()
    conn.close()
    return {"message": "Score submitted"}

# End of file
