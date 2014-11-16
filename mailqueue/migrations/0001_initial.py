# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailerMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('sent_datetime', models.DateTimeField(null=True, editable=False, blank=True)),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_email', models.EmailField(max_length=75, null=True, editable=False, blank=True)),
                ('to_email', models.EmailField(max_length=75, editable=False, db_index=True)),
                ('subject', models.TextField(verbose_name='subject')),
                ('message', models.TextField(verbose_name='plain text message')),
                ('html_message', models.TextField(default=b'', verbose_name='html message', blank=True)),
            ],
            options={
                'ordering': ('-create_datetime',),
            },
            bases=(models.Model,),
        ),
    ]
