# core/celery_schedule.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 a.m.
    "complete_classes": {
        "task": "users.tasks.complete_course",
        "schedule": crontab(hour="1", minute="0"),
        "args": (),
    },
    "generate_certificates": {
        "task": "certificates.tasks.generate_certificate",
        "schedule": crontab(hour="2", minute="30"),
        "args": (),
    },
}
