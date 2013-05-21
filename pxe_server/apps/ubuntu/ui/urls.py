from django.conf.urls import patterns, url
from ubuntu.ui.views import get_default_param

urlpatterns = patterns('',
     url(r'^$', get_default_param, name='ubuntu_preseed_param_view'),
)
