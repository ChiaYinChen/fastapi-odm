"""Formatter."""
import math
from typing import TYPE_CHECKING, Generic, TypeVar, Union

from pydantic import BaseModel

from ..repositories.base import CRUDBase
from ..schemas.pagination import Paginated, PaginationParams

if TYPE_CHECKING:
    from beanie.odm.queries.find import FindMany

DataType = TypeVar("DataType")


class GenericResponse(BaseModel, Generic[DataType]):
    """Generic wrapper for API responses."""
    message: str | None = None
    data: Union[list[DataType], DataType, None] = None
    paging: Paginated | None = None


async def paginate(
    instance: "FindMany[DataType]",
    paging_params: PaginationParams,
) -> tuple[Paginated, list[DataType]]:
    """Paginate the results of a database query."""
    # Count the total number of items matching the query
    total_counts = await CRUDBase.count(instance)

    # Calculate the total number of pages based on the total item count and items per page
    total_pages = math.ceil(total_counts / paging_params.per_page)

    # Fetch the items for the current page using skip and limit
    items = (
        await instance
        .skip(paging_params.skip)
        .limit(paging_params.limit)
        .to_list()
    )

    # Create the Paginated object that contains pagination information
    page_info = Paginated(
        current_page=paging_params.page,
        total_pages=total_pages,
        per_page=paging_params.per_page,
        total_counts=total_counts,
    )

    return page_info, items
