from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from db import db
from security import create_token

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

@app.get("/auth")
async def auth():
    row = await db.fetch_one("SELECT MAX(id) as id FROM users")
    
    max_id = (row["id"] or 0) + 1
        
    token = await create_token(max_id)
    
    await db.insert(f"INSERT INTO users (token) VALUES ({token})")
    return token