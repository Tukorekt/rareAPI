from fastapi import Header, HTTPException
from db import db
from uuid import UUID
from security import create_token


def _valide_request(token: str):
    if not token:
        raise HTTPException(status_code=404, detail="No device id")


async def get_movies_imp(jwt_token: str = Header(..., alias="X-JWT-TOKEN")):
    _valide_request(jwt_token)
        
    rows = await db.fetch_all("SELECT id, name FROM movies")
    return rows


async def auth_imp(x_device_id: UUID = Header(..., alias="X-Device-Id"),):
    if not x_device_id:
        raise HTTPException(status_code=404, detail="No device id")
    
    str_device_id = str(x_device_id)
    
    exists = await db.fetch_one("SELECT token FROM users WHERE device_id = ?", str_device_id)
    if exists["token"]:
        return exists["token"]

    row = await db.fetch_one("SELECT MAX(id) as id FROM users")
    
    max_id = (row["id"] or 0) + 1
        
    token = create_token(max_id)
    
    await db.insert("INSERT INTO users (token) VALUES ($1)", token)
    return token