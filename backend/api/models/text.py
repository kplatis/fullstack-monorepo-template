"""
Model definition for texts
"""

import uuid
from sqlalchemy import Column, UUID, String

from api.database import Base


class Text(Base):
    """
    SQLAlchemy model for text
    """

    __tablename__ = "texts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    content = Column(String, index=True, nullable=False)
    language = Column(String, index=True, nullable=False)
