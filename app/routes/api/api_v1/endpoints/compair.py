# Route definitions
from fastapi import APIRouter

router = APIRouter()

@router.get("/" )
async def get_items():
    return {"message": "items 20685"}


