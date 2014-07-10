# -*- coding: utf-8 -*-
from optparse import make_option

from django.conf import settings
from django.core.mail import mail_admins
from django.core.management.base import BaseCommand

from mailqueue import process


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--forever', dest='forever', action='store', type='bool'),
    )

    def handle(self, *args, **options):
        forever = options.get('forever')
        while True:
            try:
                process()
            except KeyboardInterrupt:
                return
            except:
                if settings.DEBUG:
                    raise
                else:
                    import traceback
                    mail_admins(__name__, traceback.format_exc())

            if not forever:
                return
