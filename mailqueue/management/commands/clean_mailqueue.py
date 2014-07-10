# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import mail_admins
from django.core.management.base import BaseCommand

from mailqueue import clean


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                clean()
            except KeyboardInterrupt:
                return
            except:
                if settings.DEBUG:
                    raise
                else:
                    import traceback
                    mail_admins(__name__, traceback.format_exc())
