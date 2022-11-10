from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    name: str
    email: str
    dob: str
    gender: str
    password: str

