# core/envs/mailgun_config.py
from pydantic import Field
from pydantic_settings import BaseSettings


class MailgunConfig(BaseSettings):
    api_key: str = Field(default_factory=lambda: "CHANGEME!!!")  # TODO check if it used or not
    domain: str = "mg.alphaedu.tech"
    from_email: str = "robot@mg.alphaedu.tech"
    from_name: str = "Robot Alphaedu Tech"
    limit_per_minute: int = 90

    class Config:
        env_prefix = "MAILGUN_"

    @property
    def base_url(self) -> str:
        return f"https://api.eu.mailgun.net/v3/{self.domain}"


mailgun_config = MailgunConfig()
