import datetime
from django.conf import settings
from django.core import mail
from django.test.utils import setup_test_environment
from django.utils import timezone
from django.test import TestCase

from ..mailqueue import add_templated_mail, MailerMessage, process, add_mail, clean
from .. import conf


class TestEmail(TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        if settings.EMAIL_BACKEND != 'django.core.mail.backends.locmem.EmailBackend':
            setup_test_environment()

        MailerMessage.objects.all().delete()
        mail.outbox = []

    def test_add_templated_email(self):
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(MailerMessage.objects.count(), 0)
        add_templated_mail('test_add_templated_email@test.test', '_test_send_templated_email.txt',
                           send_now=True)
        self.assertEqual(mail.outbox[0].subject, 'subject here')
        self.assertEqual(mail.outbox[0].body, 'body\n    here')

    def test_add_mail(self):
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(MailerMessage.objects.count(), 0)

        add_mail('subject2', 'body2', 'test_add_mail@test.test')

        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(MailerMessage.objects.count(), 1)

        process()

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(MailerMessage.objects.count(), 1)

        self.assertEqual(mail.outbox[0].subject, 'subject2')
        self.assertEqual(mail.outbox[0].body, 'body2')

    def test_clean(self):
        self.assertEqual(MailerMessage.objects.count(), 0)
        add_mail('subject3', 'body3', 'test_add_mail@test.test')
        self.assertEqual(MailerMessage.objects.count(), 1)

        MailerMessage.objects.all().update(
            sent_datetime=timezone.now() - datetime.timedelta(10),
        )

        clean()
        self.assertEqual(MailerMessage.objects.count(), 1)

        try:
            conf.MAILQUEUE_ARCHIVE_LIFETIME_DAYS = 11
            clean()
            self.assertEqual(MailerMessage.objects.count(), 1)
            conf.MAILQUEUE_ARCHIVE_LIFETIME_DAYS = 1
            clean()
            self.assertEqual(MailerMessage.objects.count(), 0)
        finally:
            conf.MAILQUEUE_ARCHIVE_LIFETIME_DAYS = 0
