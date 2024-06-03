# Route definitions
from fastapi import APIRouter
from ..api_v1.endpoints import (
    items,
    #chart,
    database,
    #user_info,
    #synastry
    )

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"], include_in_schema=True)
api_router.include_router(database.router, prefix="/database", tags=["healthcheck"])

#api_router.include_router(chart.router, prefix="/chart", tags=["healthcheck"])


#api_router.include_router(user_info.router, prefix="/user_info", tags=["user_info"])
#api_router.include_router(synastry.router, prefix="/synastry", tags=["user_info"])