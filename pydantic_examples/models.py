from typing import Optional
from pydantic import BaseModel

# Reference: https://pydantic-docs.helpmanual.io/usage/models/
# Pydantic models inherit from basemodel


class Person(BaseModel):
    name = "John Doe"
    age: int
    address: Optional[str] = None


jackson = Person(age=25, name="Jackson")
print(jackson.name)

print(jackson.dict())
print(jackson.json())

print(jackson.schema())
print(jackson.schema_json())

print(jackson.__fields__)
# returns the fields initialized during creation
print(jackson.__fields_set__)

# References
# https://pydantic-docs.helpmanual.io/usage/models/
