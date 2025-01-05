# core/views.py
import time

import redis
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse


def health_check_view(request):
    # Check database connection
    db_conn = connections["default"]
    try:
        db_conn.cursor()
        db_status = "OK"
    except OperationalError:
        db_status = "DOWN"
    except Exception as e:
        db_status = f"ERROR: {e}"

    # Check Redis connection
    try:
        r = redis.StrictRedis.from_url(settings.REDIS_CACHE_URL)
        r.ping()
        redis_status = "OK"
    except redis.ConnectionError:
        redis_status = "DOWN"
    except Exception as e:
        redis_status = f"ERROR: {e}"

    # Return JSON response
    healthcheck_dict = {
        "backend": "OK",
        "database": db_status,
        "redis": redis_status,
    }
    return JsonResponse(healthcheck_dict)


def sleep_view(request, seconds):
    time.sleep(seconds)
    return JsonResponse({"status": "OK"})
