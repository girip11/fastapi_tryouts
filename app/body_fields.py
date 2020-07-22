from typing import Optional

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter()


class BodyFieldItem(BaseModel):
    name: str
    # optional field using Field
    description: Optional[str] = Field(None, max_length=300)
    # required field using Field
    price: float = Field(..., gt=0, description="Price of the item")
    tax: Optional[float] = None
    # typ: str = Field("brand", const=True)


@router.put("/body_fields/{item_id}")
async def body_fields_validation(item_id: int, item: BodyFieldItem = Body(..., embed=True)):
    return {"item_id": item_id, "item": item}
