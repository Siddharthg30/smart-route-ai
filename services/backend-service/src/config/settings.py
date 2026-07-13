from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.
    """

    app_name: str = "SmartRoute AI Backend"
    app_version: str = "0.1.0"

    database_url: str

    host: str = "127.0.0.1"
    port: int = 8000

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """

    return Settings()