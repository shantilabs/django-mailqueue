import re
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMultiAlternatives, get_connection
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy

from mailqueue import conf
from mailqueue.utils import clean_email


class MailerMessage(models.Model):
    @classmethod
    def get_connection_settings(cls, email):
        for item in conf.MAILQUEUE_SERVER_SETTINGS:
            to_regex = item.get('to_regex', '^.*$')
            if isinstance(to_regex, basestring):
                to_regex = re.compile(to_regex)

            if to_regex.match(email):
                return dict(
                    host=item.get('host', settings.EMAIL_HOST),
                    port=item.get('port', settings.EMAIL_PORT),
                    username=item.get('username', settings.EMAIL_HOST_USER),
                    password=item.get('password', settings.EMAIL_HOST_PASSWORD),
                    use_tls=item.get('use_tls', settings.EMAIL_USE_TLS),
                )
        raise ImproperlyConfigured('Email settings for {} not found'.format(email))

    create_datetime = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    sent_datetime = models.DateTimeField(
        blank=True,
        null=True,
        editable=False,
    )
    start_datetime = models.DateTimeField(
        default=timezone.now,
    )
    from_email = models.EmailField(
        editable=False,
        blank=True,
        null=True,
    )
    to_email = models.EmailField(
        editable=False,
        db_index=True,
    )
    subject = models.TextField(ugettext_lazy('subject'))
    message = models.TextField(ugettext_lazy('plain text message'))
    html_message = models.TextField(ugettext_lazy('html message'), blank=True, default='')

    def __unicode__(self):
        return u'[{0}] {1} -> {2} [{3}]'.format(
            self.create_datetime,
            self.from_email,
            self.to_email,
            self.sent_datetime,
        )

    def send(self, get_unsbscribe_link=None):
        to_email = clean_email(self.to_email)
        connection_settings = self.get_connection_settings(to_email)
        from_email = self.from_email or connection_settings['username']
        connection = get_connection(**connection_settings)

        headers = {}
        if from_email != connection_settings['username']:
            headers.update({
                'From': conf.MAILQUEUE_FROM.format(
                    from_email=from_email,
                    email_host_user=connection_settings['username'],
                ),
                'Reply-To': self.from_email,
                'Return-Path': self.from_email,
            })

        if get_unsbscribe_link:
            headers['List-Unsubscribe'] = '<{0}>'.format(
                get_unsbscribe_link(self.to_email),
            )

        msg = EmailMultiAlternatives(
            subject=self.subject,
            body=self.message,
            from_email=None,
            to=[to_email],
            headers=headers,
            connection=connection,
        )

        if self.html_message:
            msg.attach_alternative(self.html_message, 'text/html')

        # if self.attach:
        #     assert self.attach.file.name.endswith('.xlsx'), self.attach.file.name
        #     content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        #     msg.attach(self.attach.name, self.attach.read(), content_type)

        msg.send()

        self.sent_datetime = timezone.now()
        self.save()

    class Meta:
        ordering = ('-create_datetime',)
