"""Main app."""
from contextlib import asynccontextmanager

from fastapi import FastAPI, status

from .core.logging import configure_logging
from .db.mongodb import start_async_mongodb
from .schemas.exceptions import APIValidationError


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    configure_logging()
    await start_async_mongodb()
    yield

app = FastAPI(
    lifespan=lifespan,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Validation Error",
            "model": APIValidationError
        }
    }
)
