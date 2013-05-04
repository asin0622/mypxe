from django.conf.urls import patterns, url
from ubuntu import views

urlpatterns = patterns('',
    url(r'^install/(?P<mac>([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2})/preseed.cfg$', views.get_preseed),
)
