from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'entry.views.home', name='index'),
    url(r'^register$', 'entry.views.register', name='register'),
    url(r'^login$', 'entry.views.user_login', name='login'),
    url(r'logout$', 'entry.views.user_logout', name='logout')
)