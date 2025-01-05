# core/inits/init_sentry.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from core.envs.sentry_config import sentry_config

if sentry_config.dsn:
    sentry_sdk.init(
        dsn=sentry_config.dsn,
        environment=sentry_config.env,
        traces_sampler=sentry_config.get_traces_sampler(),
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
