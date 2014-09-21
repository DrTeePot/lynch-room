# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='cancelled_election1',
            field=models.TextField(default=b'', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='cancelled_election2',
            field=models.TextField(default=b'', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='cancelled_lynches',
            field=models.TextField(default=b'', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rules',
            name='consecutive_elects',
            field=models.IntegerField(default=1, verbose_name=b'The number of election votes before cancelled votes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rules',
            name='consecutive_lynches',
            field=models.IntegerField(default=1, verbose_name=b'The number of lynch votes before cancelled votes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rules',
            name='election_count',
            field=models.IntegerField(default=0, verbose_name=b'The number of times someone can vote, 0 representing unlimited'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rules',
            name='lynch_count',
            field=models.IntegerField(default=0, verbose_name=b'The number of times someone can vote, 0 representing unlimited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rules',
            name='consensus_voting',
            field=models.BooleanField(default=False, verbose_name=b'changes the definition of majority to be consensus'),
        ),
    ]
