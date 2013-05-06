# Create your views here.
from django.http import HttpResponse
from models import Host
from django.shortcuts import render
from django.conf import settings

# just a demo 
def demo(request):
    txt = """#!ipxe
dhcp
chain http://boot.ipxe.org/demo/boot.php    
    """
    response = HttpResponse(mimetype="text/plain")
    response.content = txt
    return response

# redirect to get_mac
def default_entry(request):
    uri = request.build_absolute_uri()
    return render(request, 'boot/default.ipxe', {'uri': uri}, content_type='text/plain')

def dispatcher(request, mac):    
    host, created = Host.objects.get_or_create(_mac=mac)
    uri = request.build_absolute_uri('/')[:-1]
    return render(request, 'boot/dispatcher.ipxe', 
                  {'host': host, 'uri': uri, 'IPXE_MENUITEM': settings.IPXE_MENUITEM}, 
                  content_type='text/plain')
    
def poweroff(request, mac):
    host = Host.objects.get(_mac=mac)
    host.default_action = 'poweroff' # reboot and retry
    host.save()
    return HttpResponse('poweroff after next reboot')