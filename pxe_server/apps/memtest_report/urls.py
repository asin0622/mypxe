from django.conf.urls import patterns, url
from memtest_report import views
from boot.models import mac_pattern

urlpatterns = patterns('',
    url(r'^start/(?P<mac>%s)$' % mac_pattern, views.report_start),
    url(r'^good/(?P<mac>%s)$' % mac_pattern, views.report_good),
    url(r'^bad/(?P<mac>%s)$' % mac_pattern, views.report_bad),
    url(r'^change/(?P<mac>%s)/passes/(?P<passes>\d{1,2})' % mac_pattern, views.change_passes),
)
