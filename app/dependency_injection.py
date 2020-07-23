from typing import Any, Dict, Optional, Tuple

from fastapi import APIRouter, Cookie, Depends, Header, HTTPException
from pydantic import BaseModel

router = APIRouter()


# dependency injection can have its own hierarchy
# this method becomes the dependency of query_params
# which inturn becomes the dependency of the path operation functions
async def offset_query_params(skip: int = 0, limit: int = 10):
    return (skip, limit)


# This method can be async or non async
async def query_params(
    q: Optional[str] = None, offsets: Tuple[int, int] = Depends(offset_query_params)
):
    return {"q": q, "skip": offsets[0], "limit": offsets[1]}


# All parameters of the query_params method will be added to
# the path operation function's documentation
@router.get("/dep_inj/items/{item_id}")
async def dep_inj_items(item_id: int, query_params: Dict[str, Any] = Depends(query_params)):
    return {"item": item_id, **query_params}


# Depends accepts a Callable
@router.get("/dep_inj/users/{user_id}")
async def dep_inj_users(user_id: int, query_params: Dict[str, Any] = Depends(query_params)):
    return {"user": user_id, **query_params}


class CommonQueryParams(BaseModel):
    q: Optional[str] = None
    skip: int = 0
    limit: int = 10


# This common method can return any python object. Here it returns a pydantic model
async def query_params_model(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return CommonQueryParams(q=q, skip=skip, limit=limit)


@router.get("/dep_inj_model/items/{item_id}")
async def dep_inj_model_items(
    item_id: int, query_params: CommonQueryParams = Depends(query_params_model)
):
    print(query_params)
    return {"item": item_id, **query_params.dict()}


# Depends accepts a Callable
@router.get("/dep_inj_model/users/{user_id}")
async def dep_inj_model_users(
    user_id: int, query_params: CommonQueryParams = Depends(query_params_model)
):
    print(query_params)
    return {"user": user_id, **query_params.dict()}


# Using class as Depends since a class is also a callable
@router.get("/dep_inj_class/items/{item_id}")
async def dep_inj_class_items(
    # Depends() is same as Depends(CommonQueryParams)
    item_id: int,
    query_params: CommonQueryParams = Depends(),
):
    return {"item": item_id, **query_params.dict()}


@router.get("/dep_inj_class/users/{user_id}")
async def dep_inj_class_users(
    user_id: int, query_params: CommonQueryParams = Depends(CommonQueryParams)
):
    return {"user": user_id, **query_params.dict()}


# Dependencies in path operation decorator
# These are used when the Depends should be executed
# but they don't return a value or the value is not required
# by the path operation function. We are only concerned with the
# execution of the dependencies before the execution of path function


async def check_header_presence(user_agent: str = Header(...)):
    print(f"header value:{user_agent}")
    # we can define a condition that can raise exception
    # if not satisfied


# if the cookie is not present
# These functions can return values, but they would be
# used anywhere in the path operation function
async def check_cookie_presence(user_id: int = Cookie(...)):
    print(f"Cookie value:{user_id}")
    # we can define a condition that can raise exception
    # if not satisfied
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="user_id cookie should be > 0")


@router.get(
    "/path_op_dependencies/{item_id}",
    dependencies=[Depends(check_header_presence), Depends(check_cookie_presence)],
)
async def path_op_dependencies(item_id: int):
    pass
