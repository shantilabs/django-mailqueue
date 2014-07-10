from django.core import mail
from base import BaseTestCase

from futubank.djutils.email import send_templated_email


class TestEmail(BaseTestCase):
    def test_send_templated_email(self):
        self.assertEquals(len(mail.outbox), 0)
        send_templated_email('_test_send_templated_email.txt', 'test1@fufubank.com', ['test2@fufubank.com'])
        self.assertEquals(mail.outbox[0].subject, u'subject here')
        self.assertEquals(mail.outbox[0].body, u'body\n    here')

