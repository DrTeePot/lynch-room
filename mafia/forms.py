from mafia.models import Role, Room, Rules, Story, Message
from django import forms


class RoomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Room
        exclude = ['next_day', 'next_night']


class RulesForm(forms.ModelForm):
    class Meta:
        model = Rules


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message