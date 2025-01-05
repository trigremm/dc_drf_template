# core/envs/redis_config.py
from pydantic_settings import BaseSettings


class RedisConfig(BaseSettings):
    host: str
    port: str
    cache_url_db: int
    broker_url_db: int
    result_backend_db: int

    class Config:
        env_prefix = "REDIS_"

    @property
    def cache_url(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.cache_url_db}"

    @property
    def broker_url(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.broker_url_db}"

    @property
    def result_backend(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.result_backend_db}"


redis_config = RedisConfig()
