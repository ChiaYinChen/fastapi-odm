"""Main app."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db.mongodb import start_async_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    await start_async_mongodb()
    yield

app = FastAPI(lifespan=lifespan)
