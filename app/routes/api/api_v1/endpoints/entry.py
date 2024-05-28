from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute

from typing import Callable,  Tuple
from uuid import uuid4



router = APIRouter()

@router.get("/" )
async def dummy(request: Request):
    return {"Entry":"/"}
