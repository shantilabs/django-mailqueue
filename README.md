Install:
```
pip install -e git://github.com/shantilabs/django-mailqueue.git#egg=mailqueue
```

Base settings:
```python

INSTALLED_APPS = (
    # ...
    'mailqueue',
)
```

Optional settings:
```python

# different settings
#  a) for different recipients ("to_regex")
#  b) for mailqueue's letters and standard Django send_mail() function (used in mail_admin() etc)
MAILQUEUE_SERVER_SETTINGS = [{
    #'to_regex': '^.+$',
    #'host': EMAIL_HOST,
    #'port': EMAIL_PORT,
    #'username': EMAIL_HOST_USER,
    #'password': EMAIL_HOST_PASSWORD,
    #'use_tls' EMAIL_USE_TLS,
}]


# default behavior: synchronic send email after creation as send_mail()
MAILQUEUE_SEND_METHOD = 'now'

# send email after creation with celery task mailqueue.task.clean_mailqueue
# MAILQUEUE_SEND_METHOD = 'celery'

# Manual run
# MAILQUEUE_SEND_METHOD = 'cron'
#
# crontab: 
#   */2 * * * * www-data /path/to/my/project/manage.py process_mailqueue
# 
# or supervisord:
#   [program:myproject_mailqueue]
#   command=/path/to/my/project/manage.py process_mailqueue --forever
#   process_name=myproject_mailqueue
#   user=www-data
#   autorestart=true


# Old letters lifetime. 0 = save letters forever (default)
MAILQUEUE_ARCHIVE_LIFETIME_DAYS = 0
#
# celery: 
#   mailqueue.tasks.clean_mailqueue) 
#
# crontab: 
#   0 4 * * * www-data /path/to/my/project/manage.py clean_mailqueue

# Contents of "From" field if sender's email is not equals to server email
MAILQUEUE_FROM = "{from_email}"
# GMail always set server email to "From". Avoid this:
# MAILQUEUE_FROM = u'{from_email} <{email_host_user}>'

# Interval between letters
MAILQUEUE_PROCESSING_PAUSE_SECONDS = 2

```
