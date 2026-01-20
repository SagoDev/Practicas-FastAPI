"""Post routers"""

from fastapi import APIRouter
from ..services.post_services import fetch_posts
from ..models.post_model import Post


post_router = APIRouter(prefix="/posts", tags=["Posts"])


@post_router.get("/users/{user_id}/posts", response_model=list[Post])
async def get_user_posts(user_id: int):
    """get posts list associated to an user."""
    return await fetch_posts(user_id)
