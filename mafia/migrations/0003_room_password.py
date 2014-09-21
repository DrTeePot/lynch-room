# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0002_auto_20140921_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(default=b'', max_length=64, blank=True),
            preserve_default=True,
        ),
    ]
