from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.api.auth import get_current_user

from backend.app.models.user import User
from backend.app.models.message_schema import MessageCreate

from backend.app.services.chat_service import chat_service

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/")
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return chat_service.send_message(
        db=db,
        current_user=current_user,
        chat_id=message.chat_id,
        content=message.content
    )