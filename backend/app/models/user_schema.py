from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = {
        "from_attributes": True
    }
class UserUpdate(BaseModel):
    username: str
    email: str      
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
class UserLogin(BaseModel):
    email: str
    password: str