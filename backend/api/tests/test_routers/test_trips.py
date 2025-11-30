import uuid
from unittest.mock import patch

import pytest

from api.domain.core import ListingResult


class TestTextsRouter:
    """
    Tests for the Texts router.
    """

    @pytest.mark.asyncio
    async def test_get_text_success(self, text, test_client):
        """
        Tests successful retrieval of a text by ID.
        """

        response = await test_client.get(f"/texts/{text.id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == str(text.id)
        assert data["content"] == text.content
        assert data["language"] == text.language

    @pytest.mark.asyncio
    async def test_get_text_not_found(self, test_client):
        """
        Tests retrieval of a non-existent text by ID.
        """
        response = await test_client.get(f"/texts/{uuid.uuid4()}")

        assert response.status_code == 404
        assert response.json()["detail"] == "Text not found"

    @pytest.mark.asyncio
    async def test_get_texts_success(self, mock_texts, test_client):
        """
        Tests successful retrieval of paginated texts.
        """

        mock_result = ListingResult(items=mock_texts, total_items=5, total_pages=3)

        with patch("api.routers.text.list_texts", return_value=mock_result):
            response = await test_client.get("/texts?page=1&page_size=2")

            assert response.status_code == 200
            data = response.json()
            assert len(data["items"]) == 2
            assert data["pagination"]["total_items"] == 5
            assert data["pagination"]["total_pages"] == 3
            assert data["pagination"]["page"] == 1
            assert data["pagination"]["page_size"] == 2
            assert data["items"][0]["content"] == "Sample Text 1"
            assert data["items"][1]["content"] == "Sample Text 2"

    @pytest.mark.asyncio
    async def test_get_texts_empty_result(self, test_client):
        """
        Tests retrieval of texts when no data exists.
        """
        mock_result = ListingResult(items=[], total_items=0, total_pages=0)

        with patch("api.routers.text.list_texts", return_value=mock_result):
            response = await test_client.get("/texts")

            assert response.status_code == 200
            data = response.json()
            assert len(data["items"]) == 0
            assert data["pagination"]["total_items"] == 0
            assert data["pagination"]["total_pages"] == 0
            assert data["pagination"]["page"] == 1
            assert data["pagination"]["page_size"] == 10
