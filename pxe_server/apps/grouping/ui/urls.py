from django.conf.urls import patterns, url
from grouping.ui import views

urlpatterns = patterns('',
     url(r'^$', views.index),
     url(r'^/(?P<groupname>\w+)/hosts$', views.hosts_in_group)
)
