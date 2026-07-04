from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.models.chat import Chat
from backend.app.models.message import Message
from backend.app.services.llm_service import llm_service


class ChatService:

    def send_message(
        self,
        db: Session,
        current_user,
        chat_id: int,
        content: str
    ):

        # Verify the chat belongs to the current user
        chat = db.query(Chat).filter(
            Chat.id == chat_id,
            Chat.user_id == current_user.id
        ).first()

        if not chat:
            raise HTTPException(
                status_code=404,
                detail="Chat not found"
            )

        # Save the user's message
        user_message = Message(
            role="user",
            content=content,
            chat_id=chat_id
        )

        db.add(user_message)
        db.commit()

        # Fetch complete chat history
        history = (
            db.query(Message)
            .filter(Message.chat_id == chat_id)
            .order_by(Message.id)
            .all()
        )

        # Convert history into Gemini format
        messages = []

        for msg in history:
            messages.append(
                {
                    "role": msg.role,
                    "content": msg.content
                }
            )

        # Generate AI response
        ai_response = llm_service.generate_response(messages)

        # Save AI response
        assistant_message = Message(
            role="assistant",
            content=ai_response,
            chat_id=chat_id
        )

        db.add(assistant_message)
        db.commit()

        return {
            "response": ai_response
        }


chat_service = ChatService()