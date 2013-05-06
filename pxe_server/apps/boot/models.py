from django.db import models
import re

# Create your models here.
def validate_mac(mac):
    if not re.match('^([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2}$', mac.lower()):
        raise Exception('mac address invalid')
    return mac
    
class Host(models.Model):
    id = models.IntegerField(primary_key=True)
    _mac = models.CharField(max_length=17, unique=True, db_column='mac')
    
    # default memtest param
    max_passes = models.PositiveSmallIntegerField(default=1)
    max_test = models.PositiveSmallIntegerField(default=1)
    
    default_action = models.CharField(max_length=6, default='sleep')
    post_action = models.CharField(max_length=6, null=True)
    
    def get_mac(self):
        return self._mac
    
    def set_mac(self, mac):
        self._mac = validate_mac(mac)
    
    mac = property(get_mac, set_mac)
        
    def __unicode__(self):
        return u'Host with mac address (%s)' % self._mac
    