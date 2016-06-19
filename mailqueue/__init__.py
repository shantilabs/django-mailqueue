import logging


logger = logging.getLogger('mailqueue')

default_app_config = 'mailqueue.app.MailQueueConfig'


def add_templated_mail(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_templated_mail. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_templated_mail(...)")
    import mailqueue.mailqueue
    return mailqueue.mailqueue.add_templated_mail(*args, **kwargs)


def add_mail(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_mail. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_mail(...)")
    import mailqueue.mailqueue
    return mailqueue.mailqueue.add_mail(*args, **kwargs)


def add_glued(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.add_glued. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.add_glued(...)")
    import mailqueue.mailqueue
    return mailqueue.mailqueue.add_glued(*args, **kwargs)


def process(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.process. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.process(...)")
    import mailqueue.mailqueue
    return mailqueue.mailqueue.process(*args, **kwargs)


def clean(*args, **kwargs):
    logger.warning("Deprecated call to mailqueue.clean. Recommended way to import mailqueue: from mailqueue import mailqueue; mailqueue.clean(...)")
    import mailqueue.mailqueue
    return mailqueue.mailqueue.clean(*args, **kwargs)
