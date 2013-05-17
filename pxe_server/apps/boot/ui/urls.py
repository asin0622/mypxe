from boot.models import mac_pattern
from boot.ui import views
from boot.ui.views import HostDetail, HostList
from django.conf.urls import patterns, url

urlpatterns = patterns('',
     url(r'^$', HostList.as_view(), name='host_list_view'),
     url(r'^/(?P<mac>.+)$', HostDetail.as_view(), name='host_detail_view'),
)
