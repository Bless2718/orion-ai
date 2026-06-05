from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "OrionAI"
    VERSION: str = "1.0.0"

    OPENAI_API_KEY: str = ""
    DATABASE_URL: str = ""
    JWT_SECRET: str = ""

    class Config:
        env_file = ".env"


settings = Settings()