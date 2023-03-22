from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routes import diary_router,search_router
from app.server.exceptions import APIException

app = FastAPI()
app.include_router(diary_router.router)
app.include_router(search_router.router)

@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code =  exc.status_code,
        content = exc.content
    )
