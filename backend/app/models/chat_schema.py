from pydantic import BaseModel


class ChatCreate(BaseModel):
    title: str


class ChatResponse(BaseModel):
    id: int
    title: str
    user_id: int

    model_config = {
        "from_attributes": True
    }