from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.api.auth import get_current_user

from backend.app.models.chat import Chat
from backend.app.models.user import User
from backend.app.models.chat_schema import (
    ChatCreate,
    ChatResponse
)

router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)
@router.post(
    "/",
    response_model=ChatResponse
)
def create_chat(
    chat: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_chat = Chat(
        title=chat.title,
        user_id=current_user.id
    )

    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat
from typing import List
@router.get(
    "/",
    response_model=List[ChatResponse]
)
def get_chats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    chats = db.query(Chat).filter(
        Chat.user_id == current_user.id
    ).all()

    return chats