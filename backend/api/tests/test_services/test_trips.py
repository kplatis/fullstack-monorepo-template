from uuid import uuid4
from unittest.mock import patch
import pytest

from api.exceptions import TextNotFoundError
from api.services.text import get_text, list_texts
from api.domain.core import PaginationParams
from api.domain.core import PaginationInfo


class TestTextsService:
    """
    Unit tests for Texts service functions
    """

    @pytest.mark.asyncio
    async def test_get_text_success(self, text, main_db):
        """
        Test retrieving a text successfully.
        """
        retrieved_text = await get_text(text.id, main_db)

        assert retrieved_text.id == text.id
        assert retrieved_text.content == text.content
        assert retrieved_text.language == text.language

    @pytest.mark.asyncio
    async def test_get_text_not_found(self, main_db):
        """
        Test retrieving a non-existent text raises TextNotFoundError.
        """
        non_existent_id = uuid4()

        with pytest.raises(TextNotFoundError) as exc_info:
            await get_text(non_existent_id, main_db)

        assert str(exc_info.value) == f"Text with ID {non_existent_id} not found"

    @pytest.mark.asyncio
    async def test_list_texts_pagination(self, mock_texts, main_db):
        """
        Test listing texts with pagination using mocks.
        """

        mock_pagination_info = PaginationInfo(total_items=5, total_pages=3)

        with patch("api.services.text.retrieve_texts", return_value=mock_texts), patch(
            "api.services.text.get_total_items_of_model", return_value=mock_pagination_info
        ):

            pagination_params = PaginationParams(page=1, page_size=2)
            result = await list_texts(pagination_params, main_db)

            assert len(result.items) == 2
            assert result.total_items == 5
            assert result.total_pages == 3
            assert result.items[0].content == "Sample Text 1"
            assert result.items[1].content == "Sample Text 2"

    @pytest.mark.asyncio
    async def test_list_texts_empty_result(self, main_db):
        """
        Test listing texts when no data exists.
        """
        mock_pagination_info = PaginationInfo(total_items=0, total_pages=0)
        pagination_params = PaginationParams(page=1, page_size=10)
        with patch("api.services.text.retrieve_texts", return_value=[]), patch(
            "api.services.text.get_total_items_of_model", return_value=mock_pagination_info
        ):
            result = await list_texts(pagination_params, main_db)

            assert len(result.items) == 0
            assert result.total_items == 0
            assert result.total_pages == 0
