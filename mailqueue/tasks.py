import logging
from celery import shared_task
from mailqueue import process, clean


logger = logging.getLogger('mailqueue')


@shared_task(name='mailqueue.process')
def process_mailqueue():
    logging.info('start celery task "mailqueue.process"')
    process()


@shared_task(name='mailqueue.clean')
def clean_mailqueue():
    logging.info('start celery task "mailqueue.clean"')
    clean()
