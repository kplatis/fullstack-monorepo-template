from typing import List
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.text import Text as TextModel
from api.domain.text import TextCreate


async def create_text(text: TextCreate, db: AsyncSession) -> TextModel:
    """
    CRUD method to create a new text
    """

    db_text = TextModel(
        content=text.content,
        language=text.language,
    )

    db.add(db_text)
    await db.commit()
    await db.refresh(db_text)
    return db_text


async def retrieve_text(text_id: UUID4, db: AsyncSession) -> TextModel:
    """
    CRUD method to retrieve a text by its ID
    """
    result = await db.get(TextModel, text_id)
    return result


async def retrieve_texts(page: int, page_size: int, db: AsyncSession) -> List[TextModel]:
    """
    CRUD method to retrieve paginated texts
    """
    offset = (page - 1) * page_size
    stmt = select(TextModel).limit(page_size).offset(offset)
    result = await db.execute(stmt)
    return result.scalars().all()
