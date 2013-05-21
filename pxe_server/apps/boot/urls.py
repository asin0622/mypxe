from django.conf.urls import patterns, url
from boot import views
from boot.models import mac_pattern

urlpatterns = patterns('',
    url(r'^$', views.default_entry),
    url(r'^(?P<mac>%s)$' % mac_pattern, views.dispatcher),
    url(r'^poweroff/(?P<mac>%s)$' % mac_pattern, views.poweroff),
    url(r'^action/(?P<mac>%s)/(?P<action>\w+)$' % mac_pattern, views.change_action),
    url(r'^delete/(?P<mac>%s)' % mac_pattern, views.delete_host),
)
