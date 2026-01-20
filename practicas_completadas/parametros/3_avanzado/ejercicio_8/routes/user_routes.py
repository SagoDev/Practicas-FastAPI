"""User routes"""

from fastapi import APIRouter
from ..services.user_services import fetch_user
from ..models.user_model import User

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """get a user by id"""

    return await fetch_user(user_id)
