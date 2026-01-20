"""Main App"""

from fastapi import FastAPI
from .routes.album_routes import album_router
from .routes.post_routes import post_router
from .routes.user_routes import user_router
from .routes.user_profile_routes import user_profile_router

app = FastAPI()

app.include_router(album_router)
app.include_router(post_router)
app.include_router(user_router)
app.include_router(user_profile_router)
