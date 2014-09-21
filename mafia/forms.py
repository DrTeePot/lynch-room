from mafia.models import Role, Room, Rules, Story, Message
from django import forms


class RoomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Room
        exclude = ['owner', 'next_day', 'next_night']

class JoinRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'password']

class RulesForm(forms.ModelForm):
    class Meta:
        model = Rules
        exclude = []


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        exclude = []


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = []


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = []