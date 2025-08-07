from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./user_posts"

    class Config:
        env_file = ".env"

settings = Settings()
