"""Main App"""

from fastapi import FastAPI

from .routes import user_profile_router

app = FastAPI()

app.include_router(user_profile_router)
