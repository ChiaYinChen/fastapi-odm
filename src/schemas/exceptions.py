"""Wrapper for API Error Responses."""
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from ..consts.errors import CustomErrorCode

if TYPE_CHECKING:
    from pydantic import ValidationError


class ValidationErrorDetail(BaseModel):
    """Details of an API validation error."""
    location: str
    message: str
    error_type: str
    context: dict[str, Any] | None = None


class APIValidationError(BaseModel):
    """Wrapper for API validation errors."""
    code: str = CustomErrorCode.VALIDATE_ERROR
    message: str
    errors: list[ValidationErrorDetail]

    @classmethod
    def from_pydantic(cls, exc: "ValidationError") -> "APIValidationError":
        """Create an APIValidationError instance from a Pydantic ValidationError."""
        return cls(
            code=CustomErrorCode.VALIDATE_ERROR,
            message="Pydanyic Validation Errors",
            errors=[
                ValidationErrorDetail(
                    location=" -> ".join(map(str, err["loc"])),
                    message=err["msg"],
                    error_type=err["type"],
                    context=err.get("ctx"),
                )
                for err in exc.errors()  # iterate over each error in the Pydantic ValidationError
            ],
        )


class CustomError(BaseModel):
    """JSON response model for errors raised by :class:`CustomError`."""

    code: str
    message: Any
