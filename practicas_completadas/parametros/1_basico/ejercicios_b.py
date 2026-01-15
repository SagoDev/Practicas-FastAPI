"""
FastAPI
Plan de Ejercicios - Parametros
Básicos.
"""

from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

URL = "https://jsonplaceholder.typicode.com/users/"


@app.get("/")
def root():
    """get user by id"""
    return {
        "Nombre": "Plan de ejercicios FastAPI",
        "Dificultad": "Básico",
        "tecnología": "FastAPI",
        "Estudiante": "SagoDev",
    }


# Ejercicio Nº1: Obtener todos los usuarios
@app.get("/users")
async def get_users():
    """get all users"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}")
    response.raise_for_status()
    return response.json()


# Ejercicio Nº2: Obtener un usuario según id
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """get user by id"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/{user_id}")
        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado.",
            )

        response.raise_for_status()

        return response.json()


# Ejercicio Nº3: Obtener un usuario según id
@app.get("/users/{user_id}/basic")
async def get_filtered_user_fields(user_id: int):
    """get filtered user fields"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL}/{user_id}")

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Usuario no encontrado.")

        response.raise_for_status()

        res = response.json()

        filtered_user = {
            "id": f"{res["id"]}",
            "nombre": f"{res["name"]}",
            "email": f"{res["email"]}",
        }
        return filtered_user
