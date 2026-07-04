from pydantic import BaseModel


class MessageCreate(BaseModel):
    chat_id: int
    content: str


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    chat_id: int


class Config:
        from_attributes = True