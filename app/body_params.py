from typing import Optional

from fastapi import APIRouter, Body, Path, Query
from pydantic import BaseModel

router = APIRouter()


class BodyParamItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


# Sample JSON
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }


@router.put("/body_params/{item_id}")
async def body_params(
    *,
    item_id: int = Path(..., ge=1),
    item: BodyParamItem = Body(...),
    user: Optional[User] = Body(None),
    q: Optional[str] = Query(None)
):
    results = {"item_id": item_id, "item": item}
    if user:
        results.update({"user": user})
    if q:
        results.update({"q": q})
    return results


# item: Item = Body(..., embed=True)
# This will expect the following JSON
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }
