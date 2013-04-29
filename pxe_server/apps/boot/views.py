# Create your views here.
from django.http import HttpResponse

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
    txt = "#!ipxe\nchain %(uri)s${mac}" % \
        { 'uri': request.build_absolute_uri() }
    response = HttpResponse(mimetype="text/plain")
    response.content = txt
    return response

def dispatcher(request, mac):
    from django.shortcuts import render
    print request.build_absolute_uri('/static/')
    return render(request, 'boot/default.ipxe', {'mac': mac}, content_type='text/plain')