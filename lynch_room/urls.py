from django.conf.urls import patterns, include, url

from django.contrib import admin
import entry

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('entry.urls'), name='index'),
    url(r'^play/', include('mafia.urls'), name='mafia'),

    url(r'^admin/', include(admin.site.urls)),
)
