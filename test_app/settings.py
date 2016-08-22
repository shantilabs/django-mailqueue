USE_I18N = True
SECRET_KEY = '12345'

INSTALLED_APPS = (
    'mailqueue',
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': ':memory:',
        'NAME': 'test.sqlite3',
        'USER': '',
        'PASSWORD': '',
    }
}

MAILQUEUE_SEND_METHOD = 'cron'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

