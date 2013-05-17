from django.conf.urls import patterns, url
from grouping.ui.views import GroupingHostList, GroupList

urlpatterns = patterns('',
     url(r'^$', GroupList.as_view(), name='group_list_view'),
     url(r'^/(?P<groupname>\w+)$', GroupingHostList.as_view(), name='host_in_group_view')
)
