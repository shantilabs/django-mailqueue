Install
=======
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

Features
========

Templates for email:
```
=== letters/hello.txt ===
{% extends "email.txt" %} 
{% block subject %}Subject{% endblock %}
{% block body %}
    Hello, {{ customer.name }}!
{% endblock %}
```

Usage:
```python
import mailqueue

# email from django templates
mailqueue.add_templated_mail(customer.email, 'letters/hello.txt', {
    'customer': customer,
})

# simple email
mailqueue.add_mail('subject', 'message', 'email@example.com')

# send now
mailqueue.add_mail('subject', 'message', 'email@example.com', 
                   send_now=True)

# send after 3 days
from datetime import timedelta 
from django.utils import timezone

start_datetime = timezone.now() + timedelta(days=3)
mailqueue.add_mail('subject', 'delayed message', 'email@example.com', 
                   start_datetime=start_datetime)

# custom "From"
mailqueue.add_mail('New question', question, manager.email, 
                   from_email=customer.email)

```


Tuning
======

Different settings 
  * for different recipients ("to_regex")
  * for mailqueue's letters and standard Django send_mail() function (used in mail_admin() etc)

```python
MAILQUEUE_SERVER_SETTINGS = [{
    #'to_regex': '^.+$',
    #'host': EMAIL_HOST,
    #'port': EMAIL_PORT,
    #'username': EMAIL_HOST_USER,
    #'password': EMAIL_HOST_PASSWORD,
    #'use_tls' EMAIL_USE_TLS,
}]
```

Sending method
--------------

```python
# default behavior: synchronic send email after creation as send_mail()
MAILQUEUE_SEND_METHOD = 'now'

# send email after creation with celery task 
# MAILQUEUE_SEND_METHOD = 'celery'

# Manual run
# MAILQUEUE_SEND_METHOD = 'cron'
```

Celery task: `mailqueue.task.clean_mailqueue`

Crontab for manual run:
```
*/2 * * * * www-data /path/to/my/project/manage.py process_mailqueue
```

Supervisord config for manual run:
```
[program:myproject_mailqueue]
command=/path/to/my/project/manage.py process_mailqueue --forever
process_name=myproject_mailqueue
user=www-data
autorestart=true
```

Cleanup
-------
```
# 0 = save letters forever (default)
MAILQUEUE_ARCHIVE_LIFETIME_DAYS = 0
```

Celery task: `mailqueue.tasks.clean_mailqueue`

Crontab:
```
0 4 * * * www-data /path/to/my/project/manage.py clean_mailqueue
```

"From" field
------------

Default contents of "From" field if sender's email is not equals to server email:
```
MAILQUEUE_FROM = "{from_email}"
```

GMail always set server email to "From". Avoid this:
```
MAILQUEUE_FROM = u'{from_email} <{email_host_user}>'
```

Interval between letters
------------------------
```
MAILQUEUE_PROCESSING_PAUSE_SECONDS = 2
```
