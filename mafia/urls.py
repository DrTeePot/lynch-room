from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'mafia.views.lobby', name='lobby'),
                       url(r'game', 'mafia.views.enter_room', name='game_room'),
                       url(r'create', 'mafia.views.create_room', name='create_room'),
                       url(r'add', 'mafia.views.add_room', name='add_room'),
                       url(r'send_message', 'mafia.views.send_message', name='send_message'),
                       url(r'get_messages', 'mafia.views.get_messages', name='retrieve_messages')
)

