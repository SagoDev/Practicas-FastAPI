"""User profile services"""

import asyncio

from ..ejercicio_8.services.post_services import fetch_posts
from ..ejercicio_8.services.album_services import fetch_albums
from ..ejercicio_8.services.user_services import fetch_user

from .cache import get_cached_user, set_user_cache


async def fetch_user_profile(user_id: int) -> dict:
    """fetch user profile"""

    cached_profile = get_cached_user(user_id)
    if cached_profile:
        return cached_profile

    user = await fetch_user(user_id)

    posts_task = fetch_posts(user_id)
    albums_task = fetch_albums(user_id)

    posts, albums = await asyncio.gather(posts_task, albums_task)

    profile = {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "post_count": len(posts),
        "album_count": len(albums),
    }

    set_user_cache(user_id, profile)
    return profile
