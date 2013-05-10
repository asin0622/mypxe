from django.conf.urls import patterns, url
from boot import views

urlpatterns = patterns('',
    url(r'^$', views.default_entry),
    url(r'^(?P<mac>([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2})$', views.dispatcher),
    url(r'^poweroff/(?P<mac>([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2})$', views.poweroff)
)
