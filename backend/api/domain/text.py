from dataclasses import dataclass


@dataclass
class Text:
    """
    DTO class representing a text
    """

    id: str
    content: str
    language: str


@dataclass
class TextCreate:
    """
    DTO class for creating a new text
    """

    content: str
    language: str
