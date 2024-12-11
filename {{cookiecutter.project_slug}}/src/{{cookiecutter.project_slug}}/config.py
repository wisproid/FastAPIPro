from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str  = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DOCS_BASIC_AUTH_USERNAME: str = "admin"
    DOCS_BASIC_AUTH_PASSWORD: str = "password"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
