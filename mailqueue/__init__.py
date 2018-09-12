import logging


logger = logging.getLogger('mailqueue')

default_app_config = 'mailqueue.app.MailQueueConfig'


def add_templated_mail(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_templated_mail. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_templated_mail(...)")
    from . import mailqueue
    return mailqueue.add_templated_mail(*args, **kwargs)


def add_mail(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_mail. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_mail(...)")
    from . import mailqueue
    return mailqueue.add_mail(*args, **kwargs)


def add_glued(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_glued. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_glued(...)")
    from . import mailqueue
    return mailqueue.add_glued(*args, **kwargs)


def process(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.process. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.process(...)")
    from . import mailqueue
    return mailqueue.process(*args, **kwargs)


def clean(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.clean. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.clean(...)")
    from . import mailqueue
    return mailqueue.clean(*args, **kwargs)
