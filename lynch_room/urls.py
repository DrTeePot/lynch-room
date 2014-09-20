from django.conf.urls import patterns, include, url

from django.contrib import admin
import infosite

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('infosite.urls'), name='index'),
    url(r'^play/', include('mafia.urls'), name='mafia'),

    url(r'^admin/', include(admin.site.urls)),
)
