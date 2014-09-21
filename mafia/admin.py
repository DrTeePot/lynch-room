from django.contrib import admin
from mafia.models import Room, ChatRoom, Player, Rules, Role, Message, Story

# Register your models here.
admin.site.register(Room)
admin.site.register(ChatRoom)
admin.site.register(Player)
admin.site.register(Rules)
admin.site.register(Role)
admin.site.register(Message)
admin.site.register(Story)
