from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request, 'console/index.html')

def host_status(request):
    return render(request, 'console/host_status.html')