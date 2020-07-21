from typing import List, Optional, Set, Dict

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException


router = APIRouter()


# Always raise fastapi.HTTPException
# But handle the exception for starlette.HTTPException


@router.get("/handling_errors/{item_id}")
async def handling_errors(item_id: int):
    if item_id in range(10):
        # detail can be anything that can be converted to JSON
        # custom headers can be set as part of the response exception
        raise HTTPException(
            status_code=404,
            detail={"error": f"Item with {item_id} is not found"},
            headers={"X-Error": "Item not found"},
        )

    return {"item_id": item_id}


class CustomException(Exception):
    def __init__(self, name: str, *args: str):
        self.name = name
        self.args = args


@router.get("/custom_exception/{name}")
async def handling_custom_exceptions(name: str):
    if name != "John":
        raise CustomException(name=name)
    return {"unicorn_name": name}


# We can override default handling of exceptions like
# HTTPException, fastapi.exceptions.RequestValidationError
# RequestValidationError
# body - contains request body
# jsonable_encoder({"detail": exc.errors(), "body": exc.body})


# default exception handlers can be found in the module
# fastapi.exception_handlers
# Reference: https://fastapi.tiangolo.com/tutorial/handling-errors/#re-use-fastapis-exception-handlers

# jsonable_encoder - converts objects like Pydantic model to
# `dict` that is JSON compatible.
