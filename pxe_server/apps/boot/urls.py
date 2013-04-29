from django.conf.urls import patterns, url
from boot import views

urlpatterns = patterns('',
    url(r'^$', views.default_entry),
    url(r'^(?P<mac>([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2})$', views.dispatcher),
)
