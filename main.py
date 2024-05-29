from fastapi import  FastAPI
from pydantic import BaseModel
from typing import List
#import time

from app.routes.api.api_v1.api import api_router

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str

def create_task(id, title, description): 
    return {"id":id, "title": title, "desc": description}

@app.get("/")
async def get_items():
    id= 1
    title = "Test"
    description ="desc" 
    return create_task( id, title, description )


app.include_router(api_router)