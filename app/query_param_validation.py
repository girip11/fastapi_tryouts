from typing import List, Optional
from fastapi import APIRouter, Query


router = APIRouter()


# Optional query parameter with validations
# each query parameter can have metadata like title, description
# that will appear in the documentation.
@router.get("/query_params/{item_id}")
async def query_param_validation(
    item_id: int,
    qp: Optional[str] = Query(
        None,
        title="Query parameter",
        description="This query parameter goes through a list of validations.",
        min_length=5,
        max_length=20,
        regex=r"^[\w\s]+$",
    ),
):
    item = {"item_id": item_id, "item_name": "Dummy item"}
    if qp:
        item.update({"qp": qp})
    return item


# qp is a required parameter. Use ...(ellipsis) to indicate
# the presence of some value
# With alias, rqp from the URL will be mapped to parameter qp
@router.get("/req_query_params/")
async def req_query_param(
    qp: str = Query(..., alias="rqp", min_length=5, max_length=20, regex=r"^[\w\s]+$")
):
    return {"qp": qp}


# Multiple values for query parameter can be obtained only using
# Query. Without `Query`, query parameters will accept only primitive types.
# http://localhost:8000/items/?mvqp=foo&mvqp=bar
@router.get("/mul_val_query_params/")
async def mul_val_query_param(qp: List[str] = Query(["defaults"], alias="mvqp")):
    return {"qp": qp}


# depracated query parameters can be marked using Query(..., deprecated=True)

# Reference: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
