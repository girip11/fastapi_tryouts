from typing import Optional, Union, Dict
from fastapi import APIRouter

# This is how we can define api routes in other modules
router = APIRouter()

# Query parameters can be made required, optional by defining
# default value or marking them as Optional[Type] by assigning None

fake_items = [{"item_name": f"item_{item}"} for item in range(100)]


# http://localhost:8000/items/?skip=0&limit=10
# here mentioning skip and limit are optional
# since they have default values
@router.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    # if the skip does not have a default value set to 0
    # Then it becomes a required query parameter.
    return fake_items[skip : skip + limit]


# path parameter and query parameter
# No ordering of path and query parameters is required.
# parameters that are not in the route will be
# considered as query parameters
# Here the query parameter is optional.
@router.get("/objects/{object_id}")
async def get_items(object_id: int, qp: Optional[str] = None):
    object_dict: Dict[str, Union[int, str]] = {"object_id": object_id}
    if qp:
        object_dict.update({"q": qp})
    return object_dict
