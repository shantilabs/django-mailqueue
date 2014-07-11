import logging
import time
import datetime

from django.conf import settings
from django.utils import timezone

from mailqueue import conf
from mailqueue.models import MailerMessage
from mailqueue.utils import render_letter


logger = logging.getLogger('mailqueue')


def add_templated_mail(
    to_email,
    template,
    context=None,
    **kwargs
):
    subj, body = render_letter(template, context)
    return add_mail(subj, body, to_email, **kwargs)


def add_mail(
    subj,
    body,
    to_email,
    from_email=None,
    html_body='',
    start_datetime=None,
    send_now=False,
):
    """
    Base letter.
    """
    logger.info(u'add letter to %s with subject = %r', to_email, subj)

    if send_now or not start_datetime:
        start_datetime = timezone.now()

    if isinstance(to_email, basestring):
        to_email = [to_email]

    for t in to_email:
        obj = MailerMessage.objects.create(
            subject=subj,
            message=body,
            html_message=html_body,
            from_email=from_email,
            to_email=t,
            start_datetime=start_datetime,
        )

        if send_now or (
            conf.MAILQUEUE_SEND_METHOD == 'now' and
            obj.start_datetime <= timezone.now()
        ):
            logger.info(u'send letter #%d now', obj.id)
            obj.send()
        elif conf.MAILQUEUE_SEND_METHOD == 'celery':
            logger.info(u'send letter #%d via celery', obj.id)
            from mailqueue.tasks import process_mailqueue
            process_mailqueue.delay()
        else:
            logger.info(u'send letter #%d later', obj.id)


def add_glued(
    subj,
    body,
    from_email=None,
    to_email=[x[1] for x in settings.ADMINS],
    delay_hours=1,
):
    """
    Autoconcatenated debug letters.
    """
    if isinstance(to_email, basestring):
        to_email = [to_email]
    for t in to_email:
        obj, created = MailerMessage.objects.get_or_create(
            subject=subj,
            from_email=from_email,
            to_email=t,
            send_datetime__isnull=True,
            defaults=dict(
                message=body,
                start_datetime=timezone.now() + datetime.timedelta(delay_hours),
            ),
        )
        if not created:
            obj.message += '\n' + body
            obj.save()


def process():
    """
    Process mail queue.
    """
    logger.info('process...')
    while True:
        time.sleep(conf.MAILQUEUE_PROCESSING_PAUSE_SECONDS)
        messages = MailerMessage.objects.filter(
            send_datetime__isnull=True,
            start_datetime__lte=timezone.now(),
        )
        logger.info('%d message(s) in queue..', messages.count())
        try:
            messages[0].send()
        except IndexError:
            break

    logger.info('...process')


def clean():
    """
    Clean mail queue.
    """
    logger.info('clean...')
    lifetime_days = conf.MAILQUEUE_ARCHIVE_LIFETIME_DAYS
    logger.info('lifetime = %d day(s)', lifetime_days)
    if lifetime_days:
        deadline = timezone.now() - datetime.timedelta(lifetime_days)
        messages = MailerMessage.objects.filter(sent_datetime__lte=deadline)
        logger.info('%d message(s) to delete', messages.count())
        messages.delete()
    logger.info('...clean')
