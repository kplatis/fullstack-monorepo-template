from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.core import get_total_items_of_model
from api.crud.text import (
    create_text,
    retrieve_text,
    retrieve_texts,
)
from api.domain.core import PaginationParams
from api.exceptions import TextNotFoundError
from api.domain.core import ListingResult
from api.domain.text import Text, TextCreate
from api.settings import Settings

settings = Settings()


async def create_new_text(text_data: TextCreate, db: AsyncSession) -> Text:
    """
    Service to create a new text
    """
    new_text = await create_text(text=text_data, db=db)
    return new_text


async def get_text(text_id: UUID4, db: AsyncSession) -> Text:
    """
    Service to retrieve a text by its ID
    """
    text = await retrieve_text(text_id=text_id, db=db)
    if not text:
        raise TextNotFoundError(f"Text with ID {text_id} not found")
    return text


async def list_texts(pagination_params: PaginationParams, db: AsyncSession) -> ListingResult[Text]:
    """
    Service to list texts with pagination
    """
    texts = await retrieve_texts(page=pagination_params.page, page_size=pagination_params.page_size, db=db)
    totals = await get_total_items_of_model(Text, pagination_params.page_size, db)
    return ListingResult(items=texts, total_items=totals.total_items, total_pages=totals.total_pages)
