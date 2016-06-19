from fabric.api import local, cd, prefix, shell_env
from contextlib import contextmanager as _contextmanager
import os


root = os.path.realpath(os.path.dirname(__file__))
venv = '.env'
project = 'mailqueue'


specific_env = {
    'Darwin': dict(
        # solution of http://goo.gl/J6GEyh
        CFLAGS='-Qunused-arguments',
        CPPFLAGS='-Qunused-arguments',
    ),
}


@_contextmanager
def _virtualenv():
    if not os.path.exists(venv):
        init_venv()
    with prefix('source {}/bin/activate'.format(venv)):
        yield


def init_venv():
    with cd(root):
        local('virtualenv ' + venv)
        with _virtualenv():
            with shell_env(**specific_env.get(os.uname()[0], {})):
                local('pip install -r requirements.txt')
                local('pip install nose coverage django_nose')


def test():
    local('tox')


def build():
    with cd(root):
        with _virtualenv():
            local('python setup.py build sdist')
            local('rm -rf build')
