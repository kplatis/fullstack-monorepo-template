from pydantic import UUID4, BaseModel, ConfigDict

from api.enums import Language


class TextIn(BaseModel):
    """
    Pydantic model representing the input data for creating a text
    """

    content: str
    language: Language


class TextOut(BaseModel):
    """
    Pydantic model representing the output data for a text
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    content: str
    language: Language
