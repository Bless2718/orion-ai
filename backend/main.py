from fastapi import FastAPI
from backend.app.api.users import router as users_router
from backend.app.api.health import router as health_router
from backend.app.api.chat import router as chat_router
from backend.app.api.auth import router as auth_router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(users_router)
app.include_router(auth_router)
@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }
print("\nREGISTERED ROUTES:")

for route in app.routes:
    print(route.path)