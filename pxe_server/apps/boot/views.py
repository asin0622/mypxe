# Create your views here.
from boot import host_event, host_up
from django.http import HttpResponse
from django.shortcuts import render
from models import Host
import plugins

# just a demo 
def demo(request):
    txt = """#!ipxe
dhcp
chain http://boot.ipxe.org/demo/boot.php    
    """
    return HttpResponse(txt, mimetype="text/plain")

# redirect to get_mac
def default_entry(request):
    uri = request.build_absolute_uri()
    return render(request, 'boot/default.ipxe', {'uri': uri}, content_type='text/plain')

def dispatcher(request, mac):    
    host, created = Host.objects.get_or_create(_mac=mac)
    
    host_up.send(sender=Host, instance=host, created=created)
    host_event.send(sender=host, message='power on.')
    
    uri = request.build_absolute_uri('/')[:-1]
    return render(request, 'boot/dispatcher.ipxe', 
                  {'host': host, 'uri': uri, 'IPXE_MENUITEM': plugins.get_apps()}, 
                  content_type='text/plain')

# change action back to sleep
def poweroff(request, mac):
    host = Host.objects.get(_mac=mac)
    host_event.send(sender=host, message='power off.', action='sleep')
    return HttpResponse('change action to sleep after power')