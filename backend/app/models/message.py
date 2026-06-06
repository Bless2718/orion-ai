from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from backend.app.models.base import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id")
    )
    chat = relationship(
       "Chat",
        back_populates="messages"
)