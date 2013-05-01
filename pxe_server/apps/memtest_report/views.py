from django.http import HttpResponse
from django.shortcuts import render
from models import Host, TestResult
from datetime import datetime

def report_start(request, mac):
    host, created = Host.objects.get_or_create(_mac=mac)
    new_result = TestResult(host=host)
    new_result.save()
    return HttpResponse(host)

def record_status(mac, status):
    host = Host.objects.get(_mac=mac)
    result = host.results.all()[0]
    result.end_datetime = datetime.now()
    result.is_good = status
    result.save()
    return result

def report_good(request, mac):
    return HttpResponse(record_status(mac, True))

def report_bad(request, mac):
    return HttpResponse(record_status(mac, False))