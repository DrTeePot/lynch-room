from django.db import models
from entry.models import UserProfile
import timedelta
import datetime.datetime


class Room(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey(UserProfile, related_name='owned_rooms')
    admins = models.ManyToManyField(UserProfile, related_name='rooms_admin')
    players = models.ManyToManyField(UserProfile, related_name='rooms_joined')
    security = models.IntegerField(choices=(
        (0, "Public"),
        (1, "Password"),
        (2, "Invite Only")
    ), default=0)
    password = models.CharField(verbose_name="Only necessary when security is set to password",
                                max_length=64, blank=True, default="")

    rules = models.ForeignKey('Rules')

    next_day = models.DateTimeField(verbose_name="The next time the day will come", editable=False)
    next_night = models.DateTimeField(verbose_name="The next time the night will come", editable=False)

    def add_user(self, user):
        self.players.add(user)

    def add_admin(self, user):
        self.admins.add(user)

    def get_next_day(self):
        return self.next_day

    def get_next_night(self):
        return self.next_night


class Player(models.Model):
    userProfile = models.ForeignKey(UserProfile)
    room = models.ForeignKey('Room')

    role = models.ForeignKey('Role')

    # cancelled votes are stored as a list of player names
    lynch_votes = models.ManyToManyField('self', blank=True, null=True)
    cancelled_lynches = models.TextField(blank=True, default="", editable=False)

    election1_votes = models.ManyToManyField('self', blank=True, null=True)
    cancelled_election1 = models.TextField(blank=True, default="", editable=False)

    election2_votes = models.ManyToManyField('self', blank=True, null=True)
    cancelled_election2 = models.TextField(blank=True, default="", editable=False)


class Rules(models.Model):
    open_roles = models.IntegerField(choices=(
        (0, "Closed"),
        (1, "Open"),
        (2, "Partial")
    ), default=2)

    day_length = timedelta.fields.TimedeltaField()
    night_length = timedelta.fields.TimedeltaField()

    consensus_voting = models.BooleanField(default=False,
                                           verbose_name="changes the definition of majority to be consensus")
    lynch_count = models.IntegerField(default=0,
                                      verbose_name="The number of times someone can vote, 0 representing unlimited")
    election_count = models.IntegerField(default=0,
                                         verbose_name="The number of times someone can vote, 0 representing unlimited")
    consecutive_lynches = models.IntegerField(default=1,
                                              verbose_name="The number of lynch votes before cancelled votes")
    consecutive_elects = models.IntegerField(default=1,
                                             verbose_name="The number of election votes before cancelled votes")


class Role(models.Model):
    name = models.CharField(max_length=128)
    alignment = models.IntegerField(choices=(
        (0, "Town"),
        (1, "Mafia"),
        (2, "Psychopath"),
        (3, "Survivor")
    ), default=0)
    action = models.IntegerField(choices=(
        (0, "None"),
        (1, "Kill"),
        (2, "Save"),
        (3, "Prevent")
    ), default=0)
    action_power = models.IntegerField(default=1)
    night_move = models.BooleanField(default=False)

    use_percent = models.BooleanField(default=True)
    percent_players = models.IntegerField(verbose_name="Percent of people to get this role. "
                                                       "Must be between 0 and 100. "
                                                       "Only runs if use_percent is true")
    num_players = models.IntegerField(verbose_name="The number of people who will hold this role. "
                                                   "Only used if use_percent is false", default=0)

    auto_chatroom = models.BooleanField(
        verbose_name="Whether the people in this role should have a dedicated chat room",
        default=False)
    chatroom_name = models.CharField(verbose_name="The name of the auto chatroom if enabled", max_length=32)


class ChatRoom(models.Model):
    heading = models.CharField(max_length=32)
    members = models.ManyToManyField('Player')


class Message(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Player', related_name='messages')

    chat_room = models.ForeignKey('ChatRoom', related_name='messages')

    linked_post = models.ForeignKey('Story', blank=True, null=True, related_name='comments')
    linked_thought = models.ForeignKey('Player', blank=True, null=True, related_name='thoughts')


class Story(models.Model):
    chapter_number = models.IntegerField(editable=False)
    chapter_title = models.CharField(max_length=256)
    body = models.TextField()
