# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from .models import MailerMessage


class MailerMessageAdmin(admin.ModelAdmin):
    list_display_links = (
        'create_datetime',
    )
    list_display = (
        'id',
        'create_datetime',
        'subject',
        'from_email',
        'to_email',
        'sent_datetime',
    )
    readonly_fields = (
        'create_datetime',
        'sent_datetime',
        'subject',
        'message',
        'html_message',
        'from_email',
        'to_email',
        'start_datetime',
        'attach',
    )
    search_fields = (
        'to_email',
    )


admin.site.register(MailerMessage, MailerMessageAdmin)
