from pydantic import BaseModel, Field
from typing import Dict, Any, List
from enum import Enum

"""
In order to improve the task logic, 2 DTO classes were created:

CreateUserDTO: class responsible for data validation to create a user and has the necessary fields for this
UserDTO: class responsible for validating the User class. Has fields to retrieve all user data

"""

class UserDTO(BaseModel):
    id: int
    username: str
    email: str


class CreateUserDTO(BaseModel):
    username: str
    email: str