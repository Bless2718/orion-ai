from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "OrionAI"
    VERSION: str = "1.0.0"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str = ""
    DATABASE_URL: str = ""
    JWT_SECRET: str = ""
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
