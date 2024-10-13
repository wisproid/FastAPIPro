import os

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")

async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionFactory = async_sessionmaker(
    async_engine,
    autoflush=False,
    expire_on_commit=False,
)

async def get_db_async_session() -> AsyncGenerator: # type: ignore
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
