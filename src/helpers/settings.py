from functools import lru_cache

from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env" , env_file_encoding="utf-8")

    FILE_ALLOWED_TYPES : list[str]
    FILE_MAX_SIZE_MB : int

@lru_cache

def get_settings() -> Settings:
    return Settings()