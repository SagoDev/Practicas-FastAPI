"""User profile routes"""

from fastapi import APIRouter
from ..services.user_profile_services import fetch_user_profile
from ..models.user_profile_model import UserProfile

user_profile_router = APIRouter(prefix="/user_profile", tags=["Profiles"])


@user_profile_router.get("/user_profile/{user_id}", response_model=UserProfile)
async def get_user_profile(user_id: int):
    """get user profile"""
    return await fetch_user_profile(user_id)
