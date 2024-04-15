from pydantic import BaseModel, Field
from typing import Dict, Any, List
from enum import Enum


class UserDTO(BaseModel):
    id: int
    username: str
    email: str


class CreateUserDTO(BaseModel):
    username: str
    email: str