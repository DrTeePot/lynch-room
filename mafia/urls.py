from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'mafia.views.lobby', name='lobby'),

                       url(r'create_room', 'mafia.views.create_room', name='create_room'),
                       url(r'create_rule', 'mafia.views.create_rule', name='create_rule'),
                       url(r'create', 'mafia.views.create', name='create'),

                       url(r'add', 'mafia.views.add_room', name='join_room'),

                       url(r'send_message', 'mafia.views.send_message', name='send_message'),
                       url(r'get_messages', 'mafia.views.check_data', name='retrieve_messages'),

                       url(r'game', 'mafia.views.enter_room', name='game_room'),
                       url(r'game/vote', 'mafia.views.vote', name='vote')
)

