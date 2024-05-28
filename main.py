from fastapi import APIRouter, FastAPI, Request, Response, Header, HTTPException

from fastapi.routing import APIRoute
from uvicorn import run
from pydantic import BaseModel
from typing import List
#import time

#from app.routes.api.api_v1.api import api_router



app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str

tasks = []

def create_task(id, title, description): 
   
    return {"id":id, "title": title, "desc": description}

app = FastAPI()


@app.get("/")
async def get_items():
    id= 1
    title = "Test"
    description ="desc" 
    return create_task( id, title, description )

@app.post("/tasks/", response_model=Task)
def create_task_route(task: Task):
    id= 1
    title = "Test"
    description ="desc" 
    return create_task( id, title, description )

@app.get("/tasks/", response_model=List[Task])
def list_tasks():
    return tasks

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80, reload=True)