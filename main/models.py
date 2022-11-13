from pydantic import BaseModel
from typing import Optional, Union
from fastapi import Form

class User(BaseModel):
    name: str
    email: str
    dob: str
    gender: str
    password: str

