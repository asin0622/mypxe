from django.core.cache import get_cache
from django.db import models
import re

cache = get_cache('host')
mac_pattern = '([a-zA-Z0-9]{2}:){5}[a-zA-Z0-9]{2}'

def validate_mac(mac):
    if not re.match('^%s$' % mac_pattern, mac.lower()):
        raise Exception('mac address invalid')
    return mac
    
class ActionField(models.Field):

    description = "Default Host Action"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        self.max_length = kwargs['max_length']
        super(ActionField, self).__init__(*args, **kwargs)
        
    def db_type(self, connection):
        return 'char(%d)' % self.max_length


# refine model keep simple
class Host(models.Model):
    id = models.IntegerField(primary_key=True)
    _mac = models.CharField(max_length=17, unique=True, db_column='mac')
    
    default_action = ActionField(default='memtest')
    
    def get_mac(self):
        return self._mac
    
    def set_mac(self, mac):
        self._mac = validate_mac(mac)
    
    def set_default_action(self, action):
        self.default_action = action
        self.save()
    
    mac = property(get_mac, set_mac)
        
    def __unicode__(self):
        return u'%s' % self._mac

def _get_last_action(self):
    return cache.get(self.mac)

Host.last_action = _get_last_action
