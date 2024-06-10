"""Common dependencies."""
from fastapi import Query

from ..schemas.pagination import PaginationParams


def get_pagination_params(
    page: int = Query(1, ge=1, description="The current page number, starting from 1."),
    per_page: int = Query(10, ge=1, le=100, description="The number of items per page.")
) -> PaginationParams:
    """Get pagination parameters."""
    return PaginationParams(page=page, per_page=per_page)
