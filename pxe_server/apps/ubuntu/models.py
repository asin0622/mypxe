from django.db import models
from boot.models import Host, ActionField
from django.db.models import signals
  
class UbuntuPreseed(models.Model):
    host = models.OneToOneField(Host, related_name="preseed", primary_key=True)
     
    mirror_host = models.CharField(max_length=128, default='localhost')
    mirror_path = models.CharField(max_length=64, default='/ubuntu')
    action_after_install = ActionField(default='poweroff')
          
          
def create_mirror_config(sender, instance, created, **kwargs):
    if created:
        UbuntuPreseed.objects.create(host=instance)

signals.post_save.connect(create_mirror_config, sender=Host, weak=False,)