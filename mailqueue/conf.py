import re
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


MAILQUEUE_SERVER_SETTINGS = getattr(settings, 'MAILQUEUE_SERVER_SETTINGS', None) or [{}]

MAILQUEUE_SEND_METHOD = getattr(settings, 'MAILQUEUE_SEND_METHOD', 'now')
if not MAILQUEUE_SEND_METHOD in ('now', 'cron', 'celery'):
    raise ImproperlyConfigured('Incorrect MAILQUEUE_SEND_METHOD value')

MAILQUEUE_ARCHIVE_LIFETIME_DAYS = int(getattr(settings, 'MAILQUEUE_ARCHIVE_LIFETIME_DAYS', 0))
assert MAILQUEUE_ARCHIVE_LIFETIME_DAYS >= 0

MAILQUEUE_FROM = getattr(settings, 'MAILQUEUE_FROM', u'{from_email}')

MAILQUEUE_PROCESSING_PAUSE_SECONDS = getattr(settings, 'MAILQUEUE_PROCESSING_PAUSE_SECONDS', 2)
