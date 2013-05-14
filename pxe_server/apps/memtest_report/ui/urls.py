from django.conf.urls import patterns, url
from memtest_report.ui import views

urlpatterns = patterns('',
     url(r'^$', views.index),
)
