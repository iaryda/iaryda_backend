from fastapi import FastAPI
from .routes import diary_router,search_router

app = FastAPI()
app.include_router(diary_router.router)
app.include_router(search_router.router)
