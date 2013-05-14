from django.conf.urls import patterns, url
from boot.ui import views

urlpatterns = patterns('',
     url(r'^$', views.index),
)
