from json.decoder import JSONDecodeError

from fastapi import APIRouter, Request
from fastapi.responses import Response

from pydantic import BaseModel

from config import settings

prefix = "/ping"
router = APIRouter(prefix = prefix)


@router.get("")  # GET /ping
@router.get("/")  # GET /ping/
def ping_handler():
    print(f"INFO - GET {prefix}")
    return Response(
        content="pong",
        media_type="text/plain",
        headers={"x-powered-by": "^c+^p"}
    )


@router.post("")  # POST /ping
async def log_handler(request: Request):
    try:
        data = await request.json()
        print(f"INFO - POST {prefix} {await request.body()};")
    except JSONDecodeError as err:
        print(f"WARNING - POST {prefix} {await request.body()}; JSONDecodeError: {err}")
    except Exception as err:
        print(f"ERROR - POST {prefix} {await request.body()}; Exception: {err}")
    #else:
    #    ...
    finally:
        return Response(
            status_code=204,  # No Content
            headers={"x-powered-by": "^c+^p"},
        )
