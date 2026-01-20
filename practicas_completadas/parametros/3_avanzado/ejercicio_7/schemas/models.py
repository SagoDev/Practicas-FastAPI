"""Schemas"""

from pydantic import BaseModel


class User(BaseModel):
    """User model"""

    id: int
    name: str
    email: str
    phone: str


class Post(BaseModel):
    """Post model"""

    userId: int
    title: str
    body: str
