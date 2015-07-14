# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0002_mailermessage_attach'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailermessage',
            name='reply_to',
            field=models.EmailField(max_length=254, null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='mailermessage',
            name='from_email',
            field=models.EmailField(max_length=254, null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='mailermessage',
            name='to_email',
            field=models.EmailField(max_length=254, editable=False, db_index=True),
        ),
    ]
