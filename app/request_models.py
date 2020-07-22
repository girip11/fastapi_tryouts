from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter

# To represent request body, we can use pydantic models
# All pydantic models in the request parameter will be
# obtained from the request body.

router = APIRouter()


class RequestModelItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# JSON is automatically converted to Item model
# Each JSON field is also validated
@router.post("/items/")
async def create_item(item: RequestModelItem):
    return item


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: RequestModelItem):
    return {"item_id": item_id, **item.dict()}


# We can have a request body, query p
