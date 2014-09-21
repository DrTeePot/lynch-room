# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0004_auto_20140921_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='name',
            field=models.CharField(default='Rule', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
