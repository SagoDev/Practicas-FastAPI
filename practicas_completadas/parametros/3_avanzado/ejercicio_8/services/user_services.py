"""User Services"""

from fastapi import HTTPException
import httpx


BASE_URL = "https://jsonplaceholder.typicode.com"


async def fetch_user(
    user_id: int,
):
    """Fetch user"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/users/{user_id}")

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

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
