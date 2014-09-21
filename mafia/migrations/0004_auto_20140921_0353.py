# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0003_room_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='security',
            field=models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Password'), (2, b'Invite Only')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='password',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Only necessary when security is set to password', blank=True),
        ),
    ]
