"""Main App"""

from fastapi import FastAPI
from routers.ruoters import router

app = FastAPI()

app.include_router(router)
