from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'entry.views.home', name='index'),
    url(r'^create-user$', 'entry.views.create_user', name='create-user'),
    url(r'^login$', 'entry.views.login', name='login'),
)