from boot.models import Host, ActionField
from django.db import models
from django.db.models import signals

# default param
class DefaultMemtestParam(models.Model):
    max_passes = models.PositiveSmallIntegerField(default=1)
    max_test = models.PositiveSmallIntegerField(default=2)
    action_if_good = ActionField(default='poweroff')
    action_if_bad = ActionField(default='memtest')

def _get_default_max_passes():
    param, _ = DefaultMemtestParam.objects.get_or_create(pk=1)    
    return param.max_passes

def _get_default_max_test():
    param, _ = DefaultMemtestParam.objects.get_or_create(pk=1)
    return param.max_test

def _get_default_action_if_good():
    param, _ = DefaultMemtestParam.objects.get_or_create(pk=1)
    return param.action_if_good

def _get_default_action_if_bad():
    param, _ = DefaultMemtestParam.objects.get_or_create(pk=1)
    return param.action_if_bad

##
class MemtestParam(models.Model):
    host = models.OneToOneField(Host, related_name="memtest_params", primary_key=True)
    # default memtest param for host
    max_passes = models.PositiveSmallIntegerField(default=_get_default_max_passes)
    max_test = models.PositiveSmallIntegerField(default=_get_default_max_test)
    action_if_good = ActionField(default=_get_default_action_if_good)
    action_if_bad = ActionField(default=_get_default_action_if_bad)
        
class TestResult(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.ForeignKey(Host, related_name='results')
    
    # memtest
    is_good = models.NullBooleanField(null=True)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(null=True)
    
    # param
    max_passes = models.PositiveSmallIntegerField(default=_get_default_max_passes)
    max_test = models.PositiveSmallIntegerField(default=_get_default_max_test)
    
    class Meta:
        ordering = ["-end_datetime"]
        
    def duration(self):
        return self.end_datetime - self.start_datetime
    
    def __unicode__(self):
        res = u'Host (%s) begin test at %s, ' % (self.host._mac, self.start_datetime,)
        if not self.end_datetime:
            res += u'not finish yet'
        else:
            res += u'test finish at %s and status is %r' % (self.end_datetime, self.is_good)
        res += '<br>'            
        return res
    
def create_memtest_param(sender, instance, created, **kwargs):
    if created:
        MemtestParam.objects.create(host=instance)

signals.post_save.connect(create_memtest_param, sender=Host, weak=False,)

