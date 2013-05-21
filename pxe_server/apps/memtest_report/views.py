from boot import host_event
from boot.models import Host
from datetime import datetime
from django.http import HttpResponse
from models import TestResult

def report_start(request, mac):
    host, _ = Host.objects.get_or_create(_mac=mac)
    host_event.send(sender=host, action='memtest')
    new_result = TestResult(host=host)
    # param need?
    new_result.max_passes = host.memtest_params.max_passes
    new_result.max_test = host.memtest_params.max_test
    new_result.save()
    return HttpResponse(host)

def _record_status(mac, status):
    host = Host.objects.get(_mac=mac)
    result = host.results.order_by('-start_datetime')[0]
    result.end_datetime = datetime.now()
    result.is_good = status
    result.save()
    return result

def report_good(request, mac):
    host = Host.objects.get(_mac=mac)
    host_event.send(sender=host, message='memtest good!' % host, action=host.memtest_params.action_if_good)
    return HttpResponse(_record_status(mac, True))

def report_bad(request, mac):
    host = Host.objects.get(_mac=mac)
    host_event.send(sender=host, message='memtest bad!' % host, action=host.memtest_params.action_if_bad)
    return HttpResponse(_record_status(mac, False))

def change_passes(request, mac, passes):
    host = Host.objects.get(_mac=mac)
    host.memtest_params.max_passes = passes
    host.memtest_params.save()
    host_event.send(sender=host, message='change memtest passes to %s' % (passes))
    return HttpResponse()


