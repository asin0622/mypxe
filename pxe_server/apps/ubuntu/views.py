from django.shortcuts import render

def get_preseed(request, mac):
    return render(request, 'ubuntu/static/preseed.cfg', {}, content_type='text/plain')