from boot import host_event, host_up
from boot.models import Host
from django.core.cache import cache, get_cache
from django.db.models.signals import post_save
from django.http.response import HttpResponse, HttpResponseRedirect
from grouping.models import Group
import logging

cache = get_cache('grouping')
ALLOW_MULTIPLE_GROUP = False

# start signals
def join_exist_host(sender, instance, created, **kargs):
    groupname = cache.get('groupname')
    if groupname is None: return
    
    group = Group.objects.get(name=groupname)
    if not created:
        instance.save()
        if not ALLOW_MULTIPLE_GROUP:
            if instance.groups.count() > 0:
                return
        
        group.hosts.add(instance)
        host_event.send(sender=instance, message='new host joined group: %s' % groupname)        

def join_new_host(sender, instance, created, **kargs):
    groupname = cache.get('groupname')
    if groupname is None: return
    
    group = Group.objects.get(name=groupname)
    if created:
        instance.save()
        if not ALLOW_MULTIPLE_GROUP:
            if instance.groups.count() > 0:
                return        
        group.hosts.add(instance)
        host_event.send(sender=instance, message='new host joined group: %s' % groupname)
            
# end signals


def start_listen(request, groupname):
    Group.objects.get_or_create(name=groupname)
    cache.set('groupname', groupname)
    
    # default add exist or new added host if start listen
    host_up.connect(join_exist_host, sender=Host)
    post_save.connect(join_new_host, sender=Host)
    
    logging.info('group "%s" start listening' % groupname)
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')


def stop_listen(request, groupname):
    cache.delete('groupname')
    host_up.disconnect(join_exist_host, sender=Host)
    post_save.disconnect(join_new_host, sender=Host)
    
    logging.info('group "%s" stop listening' % groupname)
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')


def create_group(request, groupname):
    Group.objects.get_or_create(name=groupname)
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')

def delete_group(request, groupname):
    Group.objects.filter(name__exact=groupname).delete()
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect('/')

