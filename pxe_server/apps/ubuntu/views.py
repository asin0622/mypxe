from boot.models import Host
from django.shortcuts import render
from boot import host_event

def get_preseed(request, mac):
    host = Host.objects.get(_mac=mac)
    host_event.send(sender=host, action=host.preseed.action_after_install)
    return render(request, 'ubuntu/static/preseed.cfg', 
                  {'mirror_host': host.preseed.mirror_host, 
                   'mirror_path': host.preseed.mirror_path}, 
                  content_type='text/plain')