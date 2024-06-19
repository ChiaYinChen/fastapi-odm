"""Exceptions handler."""
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse

from ..main import app
from ..schemas.exceptions import APIValidationError


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    """Handle validation exceptions."""
    return ORJSONResponse(
        content=APIValidationError.from_pydantic(exc).model_dump(exclude_none=True),
        status_code=status.HTTP_400_BAD_REQUEST,
    )
