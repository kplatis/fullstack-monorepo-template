from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_db
from api.exceptions import TextNotFoundError
from api.schemas.core import PaginatedResponse, PaginationInfoOut, PaginationParamsIn
from api.domain.core import PaginationParams
from api.schemas.text import TextIn, TextOut
from api.services.text import create_new_text, get_text, list_texts

router = APIRouter()


@router.post(
    "",
    tags=["Texts"],
    response_model=TextOut,
    status_code=201,
    operation_id="createNewText",
)
async def create_new_text_endpoint(text_input: TextIn, db: AsyncSession = Depends(get_db)):
    """
    Endpoint for POST /api/texts to create a new text
    """
    text = await create_new_text(text_data=text_input, db=db)
    return TextOut.model_validate(text)


@router.get(
    "/{text_id}",
    tags=["Texts"],
    response_model=TextOut,
    status_code=200,
    operation_id="getTextById",
)
async def get_text_by_id(text_id: UUID4, db: AsyncSession = Depends(get_db)):
    """
    Endpoint for GET /api/texts/{text_id} to retrieve a text by its ID
    """
    try:
        text = await get_text(text_id=text_id, db=db)
        return TextOut.model_validate(text)
    except TextNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Text not found") from exc


@router.get(
    "",
    tags=["Texts"],
    response_model=PaginatedResponse[TextOut],
    status_code=200,
    operation_id="getTexts",
)
async def get_texts(pagination_params: PaginationParamsIn = Depends(), db: AsyncSession = Depends(get_db)):
    """
    Endpoint for GET /api/texts to list all texts
    """
    texts = await list_texts(
        pagination_params=PaginationParams(page=pagination_params.page, page_size=pagination_params.page_size), db=db
    )
    return PaginatedResponse[TextOut](
        items=[TextOut.model_validate(text) for text in texts.items],
        pagination=PaginationInfoOut(
            page=pagination_params.page,
            page_size=pagination_params.page_size,
            total_items=texts.total_items,
            total_pages=texts.total_pages,
        ),
    )
