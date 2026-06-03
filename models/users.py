from typing import Link, List, Optional

from beanie import Document
from models.events import Event
from pydantic import BaseModel, EmailStr


class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "plannerapi@gmail.com",
                "password": "strong_password_here",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "plannerapi@gmail.com",
                "password": "your_password_here"
            }
        }

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = []

    class Settings:
        name = "users"

    class Config:
            json_schema_extra = {
                "example": {
                    "email": "planner123@gmail.com ",
                    "password": "your_password_here",
                    "events": []

                }
            }
