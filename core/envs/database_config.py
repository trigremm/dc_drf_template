# core/envs/database_config.py
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    engine: str
    name: str
    user: str
    password: str
    host: str
    port: str

    class Config:
        env_prefix = "DATABASE_"


database_config = DatabaseConfig()
