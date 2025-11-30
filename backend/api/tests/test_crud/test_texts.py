from uuid import uuid4
import pytest


from api.crud.text import create_text, retrieve_text, retrieve_texts
from api.models.text import Text
from api.enums import Language


class TestTextCRUD:
    """
    Unit tests for Text CRUD operations
    """

    @pytest.mark.asyncio
    async def test_create_text(self, main_db):
        """
        Test creating a new text

        Ensures that a new text is created correctly.
        """
        text_data = Text(
            content="Hello, world!",
            language=Language.ENGLISH,
        )

        created_text = await create_text(text_data, main_db)
        assert created_text.content == "Hello, world!"
        assert created_text.language == "English"

    @pytest.mark.asyncio
    async def test_retrieve_text(self, text, main_db):
        """
        Test retrieving a text by its ID.
        """
        retrieved_text = await retrieve_text(text.id, main_db)
        assert retrieved_text.id == text.id
        assert retrieved_text.content == text.content
        assert retrieved_text.language == text.language

    @pytest.mark.asyncio
    async def test_retrieve_text_when_not_found(self, main_db):
        """
        Test retrieving a text when not found.
        """
        retrieved_text = await retrieve_text(uuid4(), main_db)
        assert retrieved_text is None

    @pytest.mark.asyncio
    async def test_retrieve_texts_pagination(self, main_db):
        """
        Test retrieving paginated texts.

        Creates multiple texts and ensures pagination works correctly.
        """
        # Create multiple texts
        texts = []
        for i in range(5):
            text_data = Text(
                content=f"Text {i}",
                language=Language.ENGLISH,
            )
            texts.append(await create_text(text_data, main_db))

        # Test first page with 2 items
        page_1 = await retrieve_texts(page=1, page_size=2, db=main_db)
        assert len(page_1) == 2
        assert page_1[0].content == "Text 0"
        assert page_1[1].content == "Text 1"

        # Test second page with 2 items
        page_2 = await retrieve_texts(page=2, page_size=2, db=main_db)
        assert len(page_2) == 2
        assert page_2[0].content == "Text 2"
        assert page_2[1].content == "Text 3"

        # Test last page with remaining items
        page_3 = await retrieve_texts(page=3, page_size=2, db=main_db)
        assert len(page_3) == 1
        assert page_3[0].content == "Text 4"

    @pytest.mark.asyncio
    async def test_retrieve_texts_empty_page(self, main_db):
        """
        Test retrieving a page when no texts exist.

        Ensures empty list is returned when no data exists.
        """
        texts = await retrieve_texts(page=1, page_size=10, db=main_db)
        assert len(texts) == 0
        assert isinstance(texts, list)
