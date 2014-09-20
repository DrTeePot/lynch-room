from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'entry.views.home'),
    url(r'^create-user$', 'entry.views.create', name='create-user'),
    url(r'^login$', 'entry.views.login', name='login'),
)