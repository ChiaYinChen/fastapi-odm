"""Wrapper for API Responses."""
from typing import Generic, TypeVar, Union

from pydantic import BaseModel

from ..schemas.pagination import Paginated

DataType = TypeVar("DataType")


class GenericResponse(BaseModel, Generic[DataType]):
    """Generic wrapper for API responses."""
    message: str | None = None
    data: Union[list[DataType], DataType, None] = None
    paging: Paginated | None = None
