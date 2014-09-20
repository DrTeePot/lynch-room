from django.db import models
from entry.models import UserProfile


# Create your models here.
class Room(models.Model):
    admins = models.ManyToManyField(UserProfile)
    players = models.ManyToManyField(UserProfile)

    rules = models.ForeignKey(Rules)


class Player(models.Model):
    userProfile = models.OneToOneField(UserProfile)
    room = models.ForeignKey(Room)

    role = models.ForeignKey(Role)

    lynch_votes = models.ManyToManyField('self', blank=True, null=True)
    election_votes = models.ManyToManyField('self', blank=True, null=True)


class Rules(models.Model):
    pass


class Role(models.Model):
    pass