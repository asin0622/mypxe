from django.conf.urls import patterns, url
from grouping import views

urlpatterns = patterns('',
    url(r'^start/(?P<groupname>\w+)$', views.start_listen),
    url(r'^stop/(?P<groupname>\w+)$', views.stop_listen),
    url(r'create/(?P<groupname>\w+)$', views.create_group),
    url(r'delete/(?P<groupname>\w+)$', views.delete_group),
)
