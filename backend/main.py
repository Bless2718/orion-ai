from fastapi import FastAPI
from backend.app.api.users import router as users_router
from backend.app.api.health import router as health_router
from backend.app.api.chat import router as chat_router
from backend.app.api.auth import router as auth_router
from backend.app.core.config import settings
from backend.app.api.chats import router as chats_router
from backend.app.api.messages import router as messages_router
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(chats_router)
app.include_router(messages_router)
@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }
