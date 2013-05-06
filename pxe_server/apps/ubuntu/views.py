from django.shortcuts import render

def get_preseed(request, mac):
    return render(request, 'ubuntu/static/preseed.cfg', 
                  {'mirror_host': '192.168.54.1:8080', 
                   'mirror_path': '/ubuntu',
                   'primary_interface': 'eth0'}, 
                  content_type='text/plain')