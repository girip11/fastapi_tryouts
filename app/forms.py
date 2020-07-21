from typing import List, Optional, Set, Dict

from fastapi import APIRouter, Form, File, UploadFile
from pydantic import BaseModel

router = APIRouter()

# With Form we can do validations on the data.
@router.post("/login_form/")
async def login(username: str = Form(...), password: str = Form(...)):
    print(password)
    return {"user_name": username, "status": "success"}


# default form data encoding is application/x-www-form-urlencoded
# When form contains files like images, the form data encoding is multipart/form-data.
# Use File to read mutipart data and Form to read the form data.
# You can define files and form fields at the same time using File and Form

# Remember Form is also a body. So you cannot use a Body parameter in
# the function as per HTTP protocol.


# In this case the conten of the file are read as bytes
# Entire file is kept in memory and hence this technique is suitable
# for smaller files.
@router.post("/upload_small_files/")
async def upload_small_files(file: bytes = File(...)):
    return {"message": len(file)}


# This is the preferred way to reading large sized files
# Here it uses a spooled file (i.e) some in memory and rest on the disk
@router.post("/upload_large_files/")
async def upload_large_file(file: UploadFile = File(...)):
    return {"message": file.filename}


# We can also fetch file metadata from UploadFile
# UploadFile has useful attributes like
# filename, content_type, file(file like object). This file object
# is used inside non async functions

# Async read and write methods on which we need to await.
# write(data:Union[str, bytes])
# read(size: int) - reads bytes
# close -  closes the file.

# Multiple uploaded files
# List[bytes]
# List[UploadFile]
