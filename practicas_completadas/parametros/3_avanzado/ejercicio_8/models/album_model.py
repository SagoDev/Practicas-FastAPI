"""Album model"""

from pydantic import BaseModel


class Album(BaseModel):
    """Album Model"""

    userId: int
    id: int
    title: str
