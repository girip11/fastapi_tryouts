from typing import Optional, List
from fastapi import APIRouter, Cookie, Header

router = APIRouter()


# Cookies can have parameter validation and data type conversion
# similar Path, Body, Query
@router.get("/cookie_params/")
async def get_cookie_params(dummy_cookie: Optional[str] = Cookie(None)):
    return {"dummy_cookie": dummy_cookie}


# NOTE: So, by default, Header will convert the parameter names
# characters from underscore (_) to hyphen (-) to extract and
#  document the headers.
# HTTP Headers are case sensitive. We should use snake_case
# version in the parameter name. user_agent will be mapped to User-Agent.
# curl -X GET "http://localhost:8000/header_params/" -H  "accept: application/json" -H "X-Token: dummy1" -H "X-TOKEN: dummy2" -H "custom_header: John"
@router.get("/header_params/")
async def get_header_params(
    user_agent: Optional[str] = Header(None),
    custom_header: Optional[str] = Header(None, convert_underscores=False),
    # duplicate headers using List
    x_token: Optional[List[str]] = Header(None),
):
    print(x_token)
    # convert_underscores will not convert hyphens in the header to underscores
    # Which means the header name will contain underscore for the mapping to work
    return {"user_agent": user_agent, "custom_header": custom_header, "x-token": x_token}


# How do I set a cookie and header in a response?
