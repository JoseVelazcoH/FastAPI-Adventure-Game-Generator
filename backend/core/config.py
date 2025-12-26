from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str
    API_PREFIX: str
    DEBUG:bool = False
    ALLOWED_ORIGINS: str = ""
    OPENAI_API_KEY: str = ""

    @field_validator("ALLOWED_ORIGINS")
    def split_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

settings = Settings()
