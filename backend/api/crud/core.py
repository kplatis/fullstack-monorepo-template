"""
Crud actions for main app functionalities
"""

from math import ceil
from typing import Generic, TypeVar
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.core import PaginationInfo

T = TypeVar("T")


async def get_total_items_of_model(model: Generic[T], page_size: int, db: AsyncSession) -> PaginationInfo:
    """
    Retrieves the total items and pages of the model
    """
    result = await db.execute(select(func.count()).select_from(model))
    total_items = result.scalar()
    total_pages = ceil(total_items / page_size)
    return PaginationInfo(total_items=total_items, total_pages=total_pages)
