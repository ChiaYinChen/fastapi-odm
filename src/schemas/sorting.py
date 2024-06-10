"""Schema for Sorting."""
from enum import Enum

from beanie.odm.enums import SortDirection
from pydantic import BaseModel, Field


class SortOrder(Enum):

    ASC = "asc"
    DESC = "desc"

    def __int__(self) -> int:
        """Converts the enum to an integer to be used by MongoDB."""
        return 1 if self.value == "asc" else -1

    @property
    def direction(self) -> SortDirection:
        return SortDirection(int(self))


class SortingParams(BaseModel):
    """Parameters used for sorting control."""
    sort: str = Field("created_at", description="The field to sort by.")
    order: SortOrder = Field(SortOrder.ASC, description="The sorting order.")
