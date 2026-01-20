"""Albums Router"""

from fastapi import APIRouter
from ..services.album_services import fetch_albums
from ..models.album_model import Album

album_router = APIRouter(prefix="/albums", tags=["Albums"])


@album_router.get("/users/{user_id}/albums", response_model=list[Album])
async def get_user_albums(user_id: int):
    """get albums list associated to an user."""
    return await fetch_albums(user_id)
