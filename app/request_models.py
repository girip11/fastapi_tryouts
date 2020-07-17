from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter

# To represent request body, we can use pydantic models

request_model_router = APIRouter()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@request_model_router.post("/items/")
async def create_item(item: Item):
    return item


@request_model_router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# We can have a request body, query p
