from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(prefix = "/ping")

@router.get("")
@router.get("/")
def ping_handler():
    return Response(
        content="pong",
        media_type="text/plain",
        headers={"x-powered-by": "^c+^p"}
    )
