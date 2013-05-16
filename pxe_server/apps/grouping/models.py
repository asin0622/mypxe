from boot.models import Host
from django.db import models

class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    hosts = models.ManyToManyField(Host, related_name='groups')
    
    def __unicode__(self):
        return u'Group "%s" contain (%d) hosts' % (self.name, self.hosts.count())