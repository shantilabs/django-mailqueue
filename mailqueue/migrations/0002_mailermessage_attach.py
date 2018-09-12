# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailermessage',
            name='attach',
            field=models.FileField(upload_to=b'attach', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
