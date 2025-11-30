from typing import Generic, TypeVar, List
from pydantic import BaseModel


T = TypeVar("T")


class PaginationParamsIn(BaseModel):
    """
    Pydantic model representing pagination parameters
    """

    page: int = 1
    page_size: int = 10


class PaginationInfoOut(BaseModel):
    """
    Pydantic model representing pagination information
    """

    page: int
    page_size: int
    total_items: int
    total_pages: int


class PaginatedResponse(BaseModel, Generic[T]):
    """
    Pydantic model representing a paginated response
    """

    items: List[T]
    pagination: PaginationInfoOut
