from fastapi import FastAPI
from src.backend.game_logic import router as game_logic_router

app = FastAPI()

app.include_router(game_logic_router)
