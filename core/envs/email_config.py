# core/envs/email_config.py
from pydantic_settings import BaseSettings


class EmailConfig(BaseSettings):
    host: str
    port: int
    use_tls: bool = False
    use_ssl: bool = False
    user: str
    password: str
    applications_to_email: str | None = None
    debug_bcc_email: str | None = None

    class Config:
        env_prefix = "EMAIL_"


email_config = EmailConfig()
