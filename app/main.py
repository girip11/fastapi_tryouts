# from dataclasses import dataclass
import importlib
from enum import Enum
from fastapi import FastAPI

import app as app_pkg


app = FastAPI()


# python dataclasses not supported
# Only pydantic dataclasses are supported
# @dataclass
# class Person:
#     name: str
#     age: int


# defines api for route /
# We can also use normal function instead of async def
@app.get("/")
async def root():
    return {"message": "Hello World"}


# item_id from the URL is automatically converted to int.
# FastAPI does automatic data conversion and data validation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Fixed paths/routes should come before parameterised paths/routes
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "Current User"}


# name of the parameter in the route and the function parameter name
# should match.
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Using enumerations for API parameters to restrict the possible
# values the parameter can take.


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Enum can be used as path parameter
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name.value, "description": f"{model_name} is an ML model"}


# path parameters can contain file paths as values
# Ex: /files//home/johndoe/myfile.txt, file_path = /home/johndoe/myfile.txt
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path, "content": "random content"}


# All modules that have router instance
# needs to include their routers in this app instance

for module in app_pkg.__all__:
    if module not in ["main"]:
        module_obj = importlib.import_module(f"{app_pkg.__name__}.{module}")
        app.include_router(getattr(module_obj, "router"))
