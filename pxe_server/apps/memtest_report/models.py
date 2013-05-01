import re
from django.db import models

def validate_mac(mac):
    if not re.match('^([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2}$', mac.lower()):
        raise Exception('mac address invalid')
    return mac
    
    
class Host(models.Model):
    id = models.IntegerField(primary_key=True)
    _mac = models.CharField(max_length=17, unique=True, db_column='mac')
    # default memtest param
    max_passes = models.PositiveSmallIntegerField(default=1)
    max_test = models.PositiveSmallIntegerField(default=4)
    
    def get_mac(self):
        return self._mac
    
    def set_mac(self, mac):
        self._mac = validate_mac(mac)
    
    mac = property(get_mac, set_mac)
        
    def __unicode__(self):
        return u'Host with mac address (%s)' % self._mac
    
        
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