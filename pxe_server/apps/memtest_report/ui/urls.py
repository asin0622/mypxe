from django.conf.urls import patterns, url
from memtest_report.ui import views
from memtest_report.ui.views import MemtestResultList

urlpatterns = patterns('',
     url(r'^$', MemtestResultList.as_view(), name='memtest_result_list_view'),
)
