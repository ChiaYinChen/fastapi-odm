"""Common dependencies."""
from fastapi import Query

from ..schemas.pagination import PaginationParams
from ..schemas.sorting import SortingParams, SortOrder


def get_pagination_params(
    page: int = Query(1, ge=1, description="The current page number, starting from 1."),
    per_page: int = Query(10, ge=1, le=100, description="The number of items per page.")
) -> PaginationParams:
    """Get pagination parameters."""
    return PaginationParams(page=page, per_page=per_page)


def get_sorting_params(
    sort: str = Query("created_at", description="The field to sort by"),
    order: SortOrder = Query(SortOrder.ASC, description="The sorting order.")
) -> SortingParams:
    """Get sorting parameters."""
    return SortingParams(sort=sort, order=order)
