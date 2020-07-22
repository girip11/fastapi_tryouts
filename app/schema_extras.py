from typing import Optional

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter()

# OpenAPI(https://swagger.io/specification/)
# has **example** field that will be used by the docsUI for
# documentation purposes.

# In pydantic model, you will use Config and schema_extra
# In Field, Path, Query and Body, we will used example=""
# which will be passed as an extra attribute


class SchemaExtrasItem(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@router.put("/schema_extras/{item_id}")
async def schema_extras(
    item_id: int,
    item: SchemaExtrasItem = Body(
        ..., example={"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2},
    ),
):
    return {"item_id": item_id, "item": item}


# References: https://fastapi.tiangolo.com/tutorial/extra-data-types/
# Other data types supported
# 1. uuid.UUID
# 2. datetime.date, datetime.datetime(timestamp),
# datetime.time(Only time), datetime.timedelta(time interval)
# 3. Decimal, bytes, frozenset
