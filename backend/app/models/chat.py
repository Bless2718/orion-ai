from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from backend.app.models.base import Base

class Chat(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user = relationship(
        "User",
        back_populates="chats"
)

    messages = relationship(
        "Message",
         back_populates="chat"
)