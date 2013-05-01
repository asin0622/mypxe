from django.conf.urls import patterns, url
from memtest_report import views

urlpatterns = patterns('',
    url(r'^start/(?P<mac>([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2})$', views.report_start),
    url(r'^good/(?P<mac>([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2})$', views.report_good),
    url(r'^bad/(?P<mac>([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2})$', views.report_bad),
)
