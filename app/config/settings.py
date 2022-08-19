import os
from pathlib import Path

from dotenv import load_dotenv

from app.config import config

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv(
    "JWT_PRIVATE_KEY",
    "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS",
)
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRES_IN", "60")
ENVIRONMENT = os.getenv("ENVIRONMENT")

API_PREFIX = "/api"

BASE_PATH = os.getenv("BASE_PATH")


class Settings:
    def __init__(self, env):
        self.env = env

    def get_config_env(self):
        base_path = os.getcwd()
        path = f"{base_path}/app/config/config_env.yml"
        yml = config.YMLConfig(
            env=self.env,
            config_file_path=path,
        )
        yml.get_yml_config()
        return yml.yml_config


if ENVIRONMENT:
    setting = Settings(env=ENVIRONMENT)
else:
    setting = Settings(env="default")
