from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from db import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/movies")
async def get_movies():
    rows = await db.fetch_all("SELECT id, name FROM movies")
    return rows

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     row = await db.fetch_one(
#         "SELECT id, name, email FROM users WHERE id = $1",
#         user_id,
#     )
#     if not row:
#         raise HTTPException(status_code=404, detail="User not found")
#     return row