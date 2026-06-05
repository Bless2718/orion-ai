from fastapi import APIRouter

from backend.app.models.chat import (
    ChatRequest,
    ChatResponse
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(request: ChatRequest):

    return ChatResponse(
        answer=f"You asked: {request.question}"
    )