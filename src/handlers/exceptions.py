"""Exceptions handler."""
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
