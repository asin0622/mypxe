from django.shortcuts import render
from ubuntu.models import DefaultPreseedParam

def get_default_param(request):
    param, _ = DefaultPreseedParam.objects.get_or_create(pk=1)
    return render(request, 'ubuntu/preseed_param.html', {'param': param})