from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
items_db = []

# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

@app.get("/")
async def server_message():
    return {"message": "server started"}


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    # Check if item already exists
    if any(existing_item["id"] == item.id for existing_item in items_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items_db.append(item.dict())
    return item

@app.get("/items", response_model=List[Item])
async def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db[index] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
