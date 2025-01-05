# core/envs/sentry_config.py
from pydantic import Field
from pydantic_settings import BaseSettings


class SentryConfig(BaseSettings):
    dsn: str | None = None
    env: str = "local"
    error_sample_rate: float = Field(default=1.0, ge=0, le=1)
    default_sample_rate: float = Field(default=0.01, ge=0, le=1)

    class Config:
        env_prefix = "SENTRY_"

    def get_traces_sampler(self):
        def traces_sampler(context):
            if context.get("parent_sampled") is False:
                return self.error_sample_rate
            return self.default_sample_rate

        return traces_sampler


sentry_config = SentryConfig()
