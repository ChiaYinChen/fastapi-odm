"""Main app."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .core.logging import configure_logging
from .db.mongodb import start_async_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    configure_logging()
    await start_async_mongodb()
    yield

app = FastAPI(lifespan=lifespan)
