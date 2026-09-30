from contextlib import asynccontextmanager
from fastapi import FastAPI, Header
from db import db
from uuid import UUID
from routes import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/movies")
async def get_movies(jwt_token: str = Header(..., alias="X-JWT-Token")):
    get_movies_imp(jwt_token)

@app.get("/auth")
async def auth(x_device_id: UUID = Header(..., alias="X-Device-Id"),):
    auth_imp(x_device_id)