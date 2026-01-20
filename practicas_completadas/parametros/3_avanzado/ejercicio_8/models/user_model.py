"""User Model"""

from pydantic import BaseModel


class User(BaseModel):
    """User Model"""

    id: int
    name: str
    email: str
    phone: str
