from typing import Optional

from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter()


class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ItemOut(BaseModel):
    name: str
    price: float
    tax: Optional[float] = None


# status_code can alternatively also receive an IntEnum,
# such as Python's http.HTTPStatus
# This status code also get OpenAPI documentation.
@router.post(
    "/response_models/{item_name}",
    summary="Summary of this API",
    response_description="Description of the response model",
    response_model=ItemOut,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
)
async def create_response_models(item: ItemIn):
    """This docstring becomes the description of this API

    Args:
        item (ItemIn): [description]

    Returns:
        [type]: [description]
    """
    # fastapi can automatically convert request model to response model
    # using pydantic.
    # Request and response model attribute names should match for this mapping
    # to work automatically.
    return item


# to omit the optional fields that are not set, we can set
# response_model_exclude_unset= True in the router decorator.
# We can also use
# response_model_exclude_defaults=True
# response_model_exclude_none=True
# response_model_include and response_model_exclude - set of attribute names in the models


# You can declare a response to be the (from typing module) Union
# of two types, that means, that the response would be any of the two.
# When defining a Union, include the most specific type first,
# followed by the less specific type.
# response can also contain list of response models.

# Response with arbitrary dict (typing.Dict)
# This is useful if you don't know the valid field/attribute
# names (that would be needed for a Pydantic model) beforehand.


# Path operation configuration
# https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
