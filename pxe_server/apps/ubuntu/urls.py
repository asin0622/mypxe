from django.conf.urls import patterns, url
from ubuntu import views
from boot.models import mac_pattern

urlpatterns = patterns('',
    url(r'^install/(?P<mac>%s)/preseed.cfg$' % mac_pattern, views.get_preseed),
)
