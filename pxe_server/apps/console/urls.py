from django.conf.urls import patterns, url, include
from console import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='home'),
     url(r'^host_status', include('boot.ui.urls')),
     url(r'^memtest', include('memtest_report.ui.urls')),
     url(r'^group', include('grouping.ui.urls')),
)
