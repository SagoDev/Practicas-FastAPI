"""DTO Profile Model"""

from pydantic import BaseModel


class UserProfile(BaseModel):
    """Profile Model"""

    id: int
    name: str
    email: str
    post_count: int
    album_count: int
