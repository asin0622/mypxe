from django.conf.urls import patterns, url
from grouping import views

urlpatterns = patterns('',
    url(r'^start/(?P<groupname>\w+)$', views.start_listen),
    url(r'^stop/(?P<groupname>\w+)$', views.stop_listsn),
)
