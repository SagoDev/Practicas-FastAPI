"""Post Services"""

from fastapi import HTTPException
import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"


async def fetch_posts(user_id: int) -> list[dict]:
    """Fetch user post"""
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(
                f"{BASE_URL}/posts/", params={"user_id": user_id}
            )

            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException as timeout_exc:
        raise HTTPException(
            status_code=504, detail="Servicio externo no responde."
        ) from timeout_exc

    except httpx.RequestError as req_exc:
        raise HTTPException(
            status_code=502, detail="Servicio externo no disponible."
        ) from req_exc
