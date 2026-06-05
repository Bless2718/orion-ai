from backend.app.core.database import engine
from backend.app.models.base import Base

# Import models
from backend.app.models.user import User


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")