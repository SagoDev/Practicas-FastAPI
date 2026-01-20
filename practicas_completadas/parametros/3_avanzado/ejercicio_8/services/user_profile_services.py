"""User profile services"""

import asyncio
from fastapi import HTTPException
import httpx

from .user_services import fetch_user
from .album_services import fetch_albums
from .post_services import fetch_posts


async def fetch_user_profile(user_id: int) -> dict:
    """Fetch user profile"""
    try:
        user = await fetch_user(user_id)
        albums_task = fetch_albums(user_id)
        posts_task = fetch_posts(user_id)

        posts, albums = await asyncio.gather(posts_task, albums_task)

        return {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "post_count": len(posts),
            "album_count": len(albums),
        }

    except httpx.TimeoutException as timeout_exc:
        raise HTTPException(
            status_code=504, detail="Servicio externo no responde."
        ) from timeout_exc

    except httpx.RequestError as req_exc:
        raise HTTPException(
            status_code=502, detail="Servicio externo no disponible."
        ) from req_exc
