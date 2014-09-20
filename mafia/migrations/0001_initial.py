# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timedelta.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('election1_votes', models.ManyToManyField(related_name='election1_votes_rel_+', null=True, to='mafia.Player', blank=True)),
                ('election2_votes', models.ManyToManyField(related_name='election2_votes_rel_+', null=True, to='mafia.Player', blank=True)),
                ('lynch_votes', models.ManyToManyField(related_name='lynch_votes_rel_+', null=True, to='mafia.Player', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('alignment', models.IntegerField(default=0, choices=[(0, b'Town'), (1, b'Mafia'), (2, b'Psychopath'), (3, b'Survivor')])),
                ('action', models.IntegerField(default=0, choices=[(0, b'None'), (1, b'Kill'), (2, b'Save'), (3, b'Prevent')])),
                ('action_power', models.IntegerField(default=1)),
                ('night_move', models.BooleanField(default=False)),
                ('use_percent', models.BooleanField(default=True)),
                ('percent_players', models.IntegerField(verbose_name=b'Percent of people to get this role. Must be between 0 and 100. Only runs if use_percent is true')),
                ('num_players', models.IntegerField(default=0, verbose_name=b'The number of people who will hold this role. Only used if use_percent is false')),
                ('auto_chatroom', models.BooleanField(default=False, verbose_name=b'Whether the people in this role should have a dedicated chat room')),
                ('chatroom_name', models.CharField(max_length=32, verbose_name=b'The name of the auto chatroom if enabled')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('next_day', models.DateTimeField(verbose_name=b'The next time the day will come', editable=False)),
                ('next_night', models.DateTimeField(verbose_name=b'The next time the night will come', editable=False)),
                ('admins', models.ManyToManyField(related_name=b'rooms_admin', to='entry.UserProfile')),
                ('owner', models.ForeignKey(related_name=b'owned_rooms', to='entry.UserProfile')),
                ('players', models.ManyToManyField(related_name=b'rooms_joined', to='entry.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open_roles', models.IntegerField(default=2, choices=[(0, b'Closed'), (1, b'Open'), (2, b'Partial')])),
                (b'day_length', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                (b'night_length', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('consensus_voting', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter_number', models.IntegerField(editable=False)),
                ('chapter_title', models.CharField(max_length=256)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='room',
            name='rules',
            field=models.ForeignKey(to='mafia.Rules'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.ForeignKey(to='mafia.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='room',
            field=models.ForeignKey(to='mafia.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='userProfile',
            field=models.ForeignKey(to='entry.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(related_name=b'messages', to='mafia.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='chat_room',
            field=models.ForeignKey(related_name=b'messages', to='mafia.ChatRoom'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='linked_post',
            field=models.ForeignKey(related_name=b'comments', blank=True, to='mafia.Story', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='linked_thought',
            field=models.ForeignKey(related_name=b'thoughts', blank=True, to='mafia.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(to='mafia.Player'),
            preserve_default=True,
        ),
    ]
