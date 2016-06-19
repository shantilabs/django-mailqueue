from distutils.core import setup


setup(
    name='django-mailqueue',
    version='0.1',
    author='Maxim Oransky',
    author_email='maxim.oransky@gmail.com',
    url='https://github.com/shantilabs/django-mailqueue',
    packages=[
        'mailqueue',
        'mailqueue.migrations',
        'mailqueue.tests',
    ],
    package_data={
        'mailqueue': ['templates/*'],
    },
)
