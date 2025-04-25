import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from config import settings
from handlers.ping import router as ping_router


app = FastAPI()
app.include_router(ping_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"https://{settings.API_DOMAIN}",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom handler for 404 Not Found
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return Response(
            status_code=204,  # No Content
            headers={"x-powered-by": "^c+^p"},
        )
    return Response(content=str(exc.detail), status_code=exc.status_code)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=f"{settings.API_IPADDRESS}",
        port=settings.API_PORT,
        log_level=settings.log_level,
        reload=settings.RELOAD,
    )
