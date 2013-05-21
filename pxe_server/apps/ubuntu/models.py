from django.db import models
from boot.models import Host, ActionField
from django.db.models import signals
  
class DefaultPreseedParam(models.Model):
    mirror_host = models.CharField(max_length=128, default='localhost')
    mirror_path = models.CharField(max_length=64, default='/ubuntu')
    action_after_install = ActionField(default='poweroff')
    
def _get_default_mirror_host():
    param, _ = DefaultPreseedParam.objects.get_or_create(pk=1)
    return param.mirror_host

def _get_default_mirror_path():
    param, _ = DefaultPreseedParam.objects.get_or_create(pk=1)
    return param.mirror_path


def _get_default_action_after_install():
    param, _ = DefaultPreseedParam.objects.get_or_create(pk=1)
    return param.action_after_install

class UbuntuPreseed(models.Model):
    host = models.OneToOneField(Host, related_name="preseed", primary_key=True)
     
    mirror_host = models.CharField(max_length=128, default=_get_default_mirror_host)
    mirror_path = models.CharField(max_length=64, default=_get_default_mirror_path)
    action_after_install = ActionField(default=_get_default_action_after_install)
          
          
def create_mirror_config(sender, instance, created, **kwargs):
    if created:
        UbuntuPreseed.objects.create(host=instance)

signals.post_save.connect(create_mirror_config, sender=Host, weak=False,)