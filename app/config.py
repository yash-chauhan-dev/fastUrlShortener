from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_host: str = Field(..., env="MONGO_DB_HOST")
    db_str: str = Field(..., env="DATABASE_NAME")
    db_collection_str: str = Field(..., env="COLLECTION_NAME")
    app_host: str = Field(..., env="APP_HOST")

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
