"""
FastAPI
Ejercicio 1: Endpoint GET /users/{user_id}. Retornar el user_id
"""

from fastapi import FastAPI
import httpx

app = FastAPI()

URL = "https://jsonplaceholder.typicode.com/users/"


@app.get("/")
def root():
    """get user by id"""
    return {
        "Ejecicio": "Retornar el user_id",
        "tecnología": "FastAPI",
        "Estudiante": "SagoDev",
    }


@app.get("/get/{user_id}")
async def get_user(user_id: int):
    """get user by id"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        )
        response.raise_for_status()
        return response.json()
