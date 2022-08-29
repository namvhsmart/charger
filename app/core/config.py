from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str = "mysql+pymysql://root:123456@localhost:3306/charger"
    API_PREFIX: str = "/api"
    ORIGINS: list = ["*"]
    TITLE: str = "EV Charger"
    DESCRIPTION: str = "EV Charger Project"
    VERSION: str = "0.1.0"
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: str = 60
    ENVIRONMENT: str = "dev"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
