# core/envs/django_config.py
from pydantic import Field
from pydantic_settings import BaseSettings


class DjangoConfig(BaseSettings):
    debug: bool
    secret_key: str
    allowed_hosts: list[str] = Field(
        default_factory=lambda: [
            "alphaedu.tech",
            "www.alphaedu.tech",
            "test.alphaedu.tech",
        ],
    )
    cors_allowed_origins: list[str] = Field(
        default_factory=lambda: [
            "https://alphaedu.tech",
            "https://www.alphaedu.tech",
            "https://test.alphaedu.tech",
        ],
    )
    frontend_url: str = "https://test.alphaedu.tech"
    backend_url: str = "https://test.alphaedu.tech/api"
    time_zone: str = "Asia/Qyzylorda"

    class Config:
        env_prefix = "DJANGO_"


django_config = DjangoConfig()
