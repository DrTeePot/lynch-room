from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'mafia.views.home', name='home'),
    url(r'^lobby', 'mafia.views.lobby', name='lobby'),
)

