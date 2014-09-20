from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'infosite.views.home', name='home'),
    url(r'^create-user$', 'infosite.views.create', name='create-user'),
    url(r'^login$', 'infosite.views.login', name='login'),
)