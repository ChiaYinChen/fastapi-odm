"""Exceptions handler."""
from typing import Any

from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from ..main import app
from ..schemas.exceptions import APIValidationError


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc: RequestValidationError) -> ORJSONResponse:
    """Handle validation exceptions."""
    return ORJSONResponse(
        content=APIValidationError.from_pydantic(exc).model_dump(exclude_none=True),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


class CustomError(Exception):
    """Custom error."""

    def __init__(self, status_code: int, error_code: str, message: Any):
        """Initialize."""
        self.status_code = status_code
        self.error_code = error_code
        self.message = message


class NotFoundError(CustomError):
    """Resource not found error."""

    def __init__(self, error_code: str, message: Any):
        """Initialize."""
        self.status_code = status.HTTP_404_NOT_FOUND
        self.error_code = error_code
        self.message = message


class ConflictError(CustomError):
    """Resource conflict error."""

    def __init__(self, error_code: str, message: Any):
        """Initialize."""
        self.status_code = status.HTTP_409_CONFLICT
        self.error_code = error_code
        self.message = message


@app.exception_handler(CustomError)
async def custom_error_handler(_, exc: CustomError) -> ORJSONResponse:
    """Handle custom error."""
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"code": exc.error_code, "message": exc.message},
    )
