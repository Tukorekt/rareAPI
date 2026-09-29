import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")

class Database:
    def __init__(self):
        self.pool: asyncpg.Pool | None = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            dsn=DATABASE_URL,
            min_size=1,
            max_size=10,
        )

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch_all(self, query: str, *args):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(query, *args)
            return [dict(r) for r in rows]

    async def fetch_one(self, query: str, *args):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(query, *args)
            return dict(row) if row else None
        
    async def insert(self, query: str, *args):
            async with self.pool.acquire() as conn:
                await conn.execute(query, *args)
                

db = Database()