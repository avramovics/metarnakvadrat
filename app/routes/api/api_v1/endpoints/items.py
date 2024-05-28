# Route definitions
from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute
from pydantic import BaseModel 
from fastapi import HTTPException



from pydantic import BaseModel 
from enum import Enum



router = APIRouter()


class Category(Enum):
    TOOLS = "tools" 
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int 
    id: int  
    category: Category = None

items = {
    0: Item( name="Hammer" ,price=9.99 ,count=20 ,id=0 ,category=Category.TOOLS ),
    1: Item( name="Pliers" ,price=5.99 ,count=20 ,id=1 ,category=Category.TOOLS ),
    2: Item( name="Nails" ,price=1.99 ,count=100 ,id=2 ,category=Category.CONSUMABLES )
}



@router.get("")
def get_items():
    return items

#@router.get("/{id}" )
#def get_items(id: int) -> Item:
#    if id not in items:
#        raise HTTPException(status_code = 404, detail=f"item with id: {id} does not exist")
#    return  items[id]



@router.post("/i")
def create_or_update_item(item: Item):
    # Add the item to the dictionary with its ID as the key
    items[item.id] = item
    return item