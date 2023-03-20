from fastapi import FastAPI
from .routes import diary_router

app = FastAPI()
app.include_router(diary_router.router)
