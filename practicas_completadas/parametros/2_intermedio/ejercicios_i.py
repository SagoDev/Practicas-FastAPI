"""
FastAPI
Plan de Ejercicios - Parametros
Intermedios.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()


URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"


@app.get("/")
def root():
    """Info"""
    return {
        "Nombre": "Plan de ejercicios FastAPI",
        "Dificultad": "Intermedio",
        "tecnología": "FastAPI",
        "Estudiante": "SagoDev",
    }


# Ejercicio Nº4: Usar Pydantic para modelar usuarios


class UserBasic(BaseModel):
    """User model"""

    id: int
    name: str
    email: str
    phone: str


@app.get("/users/{user_id}/basic", response_model=UserBasic)
async def get_user_with_model(user_id: int):
    """get a user by id using pydantic model"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL_USERS}/{user_id}")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    response.raise_for_status()

    model_response = response.json()
    return model_response


# Ejercicio Nº5: Listar posts de usuarios
class Post(BaseModel):
    """Post model"""

    userId: int
    title: str
    body: str


@app.get("/posts/", response_model=list[Post])
async def get_posts_by_user(user_id: int):
    """get posts list associated to an user."""

    async with httpx.AsyncClient() as client:
        user_response = await client.get(f"{URL_USERS}/{user_id}")
        posts_response = await client.get(f"{URL_POSTS}", params={"userId": user_id})

    if user_response.status_code == 404:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    posts_response.raise_for_status()

    res = posts_response.json()

    return res


# Ejercicio Nº6: Manejo de errores externos
async def fetch_user(user_id: int):
    """Error handler function."""
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{URL_USERS}/{user_id}")

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado.")

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
