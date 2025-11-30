from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class PaginationParams:
    """
    DTO class representing pagination parameters
    """

    page: int = 1
    page_size: int = 10


@dataclass
class ListingResult(Generic[T]):
    """
    DTO class representing a paginated listing result
    """

    items: list[T]
    total_items: int
    total_pages: int


@dataclass
class PaginationInfo:
    """
    DTO class representing pagination information
    """

    total_items: int
    total_pages: int
