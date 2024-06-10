"""Schema for Pagination."""
from pydantic import BaseModel, Field


class Paginated(BaseModel):
    """Pagination metadata."""
    current_page: int = Field(1, description="Current page number being displayed.")
    total_pages: int = Field(1, description="Total pages available, calculated from the query results.")
    per_page: int = Field(10, description="Number of items displayed on each page.")
    total_counts: int = Field(0, description="Total number of items based on current query.")


class PaginationParams(BaseModel):
    """Parameters used for pagination control."""
    page: int = Field(1, ge=1, description="The current page number, starting from 1.")
    per_page: int = Field(10, ge=1, le=100, description="The number of items per page.")

    @property
    def skip(self) -> int:
        """Calculate the number of records to skip based on the current page and items per page."""
        return (self.page - 1) * self.per_page

    @property
    def limit(self) -> int:
        """Get the limit on the number of records to return, based on per_page setting."""
        return self.per_page
