from django.shortcuts import render
from boot.models import Host
from boot import host_action

def get_preseed(request, mac):
    host = Host.objects.get(_mac=mac)
    host_action.send(sender=host, action=host.preseed.action_after_install)
    return render(request, 'ubuntu/static/preseed.cfg', 
                  {'mirror_host': host.preseed.mirror_host, 
                   'mirror_path': host.preseed.mirror_path}, 
                  content_type='text/plain')