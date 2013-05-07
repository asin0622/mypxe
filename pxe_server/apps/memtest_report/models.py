from boot.models import Host, ActionField
from django.db import models
from django.db.models import signals
    

class MemtestParam(models.Model):
    host = models.OneToOneField(Host, related_name="memtest_params", primary_key=True)
    # default memtest param
    max_passes = models.PositiveSmallIntegerField(default=1)
    max_test = models.PositiveSmallIntegerField(default=2)
    action_if_good = ActionField(max_length=10, default='poweroff')
    action_if_bad = ActionField(max_length=10, default='memtest')
        
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
    
def create_memtest_param(sender, instance, created, **kwargs):
    if created:
        MemtestParam.objects.create(host=instance)

signals.post_save.connect(create_memtest_param, sender=Host, weak=False,)
