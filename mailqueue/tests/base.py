from django.conf import settings
from django.test import TestCase
from django.test.utils import setup_test_environment


class BaseTestCase(TestCase):
    def setUp(self):
        if not settings.configured:
            settings.configure()

        if settings.EMAIL_BACKEND != 'django.core.mail.backends.locmem.EmailBackend':
            setup_test_environment()
