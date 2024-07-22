"""Main app."""
from contextlib import asynccontextmanager
from http import HTTPStatus
from typing import Set

from fastapi import FastAPI, status

from .core.logging import configure_logging
from .db.mongodb import start_async_mongodb
from .schemas.exceptions import APIValidationError, CustomError


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize application services."""
    configure_logging()
    await start_async_mongodb()
    yield

# Common response codes
responses: Set[int] = {
    status.HTTP_404_NOT_FOUND,
    status.HTTP_409_CONFLICT,
    status.HTTP_500_INTERNAL_SERVER_ERROR,
}

app = FastAPI(
    lifespan=lifespan,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation Error",
            "model": APIValidationError
        },
        **{
            code: {
                "description": HTTPStatus(code).phrase,
                "model": CustomError,
            }
            for code in responses
        },
    }
)
