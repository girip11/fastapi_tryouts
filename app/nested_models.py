from typing import List, Optional, Set, Dict

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field

router = APIRouter()


class Image(BaseModel):
    # HttpUrl is also a type of str
    # other types derived from str is also supported
    url: HttpUrl
    name: str


class NestedModelItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # JSON array converted to set
    tags: Set[str] = Field(...)
    # List values
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    # Nested models support
    items: List[NestedModelItem]


# Body parameters can be JSON array
@router.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@router.post("/offers/")
async def create_offer(offer: Offer):
    return offer


# JSON only supports string as keys
# But we can use other data types as keys using fastapi
# string keys are automatically converted to integers
# (if the string data contains valid integers)
@router.post("/int_json_keys/")
async def create_int_keys(data: Dict[int, float]):
    return data
