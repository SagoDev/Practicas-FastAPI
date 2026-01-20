"""Post Model"""

from pydantic import BaseModel


class Post(BaseModel):
    """Post Model"""

    userId: int
    title: str
    body: str
