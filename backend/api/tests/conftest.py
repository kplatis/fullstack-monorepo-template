from typing import AsyncGenerator
from uuid import uuid4
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import SessionLocal, create_tables
from api.models.text import Text as TextModel


@pytest_asyncio.fixture(name="main_db")
async def db() -> AsyncGenerator[AsyncSession, None]:
    """
    Defines the main database which is empty
    """
    async with SessionLocal() as session:
        await create_tables(clear_before_create=True)
        yield session


@pytest_asyncio.fixture(name="mock_texts")
async def texts():
    """
    Defines a fixture for mock texts
    """
    return [
        TextModel(id=uuid4(), content="Sample Text 1", language="English"),
        TextModel(id=uuid4(), content="Sample Text 2", language="French"),
    ]


@pytest_asyncio.fixture
async def text(main_db: AsyncSession, mock_texts):
    """
    Defines a fixture for a single text
    """
    mock_text = mock_texts[0]
    main_db.add(mock_text)
    await main_db.commit()
    await main_db.refresh(mock_text)
    return mock_text
