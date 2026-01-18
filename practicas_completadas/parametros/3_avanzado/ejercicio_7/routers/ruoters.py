"""Routers"""

from fastapi import APIRouter
from services.jsonplaceholder import fetch_user, fetch_user_posts
from schemas.models import User, Post

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """get a user by id"""

    return await fetch_user(user_id)


@router.get("/users/{user_id}/posts", response_model=list[Post])
async def get_user_posts(user_id: int):
    """get posts list associated to an user."""
    return await fetch_user_posts(user_id)
