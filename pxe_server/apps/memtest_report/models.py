import re
from django.db import models
from boot.models import Host
        
class TestResult(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(Host, related_name='results')
    # memtest
    is_good = models.BooleanField()
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ["-start_datetime"]
        
    def __unicode__(self):
        res = u'Host (%s) begin test at %s, ' % (self.host._mac, self.start_datetime,)
        if not self.end_datetime:
            res += u'not finish yet'
        else:
            res += u'test finish at %s and status is %r' % (self.end_datetime, self.is_good)
        res += '<br>'            
        return res