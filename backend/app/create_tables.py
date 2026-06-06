from backend.app.core.database import engine
from backend.app.models.base import Base
from backend.app.models.chat import Chat
from backend.app.models.message import Message
# Import models
from backend.app.models.user import User


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")