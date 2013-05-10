from boot import host_event, host_up
from boot.models import Host
from django.core.cache import cache
from django.db.models.signals import post_save
from django.http.response import HttpResponse
from grouping.models import Group

def join_exist_host(sender, instance, created, **kargs):
    groupname = cache.get('groupname')
    group = Group.objects.get(name=groupname)
    if not created:
        instance.save()
        group.hosts.add(instance)
        host_event.send(sender=instance, message='new host joined group: %s' % groupname)        

def join_new_host(sender, instance, created, **kargs):
    groupname = cache.get('groupname')
    group = Group.objects.get(name=groupname)
    if created:
        instance.save()
        group.hosts.add(instance)
        host_event.send(sender=instance, message='new host joined group: %s' % groupname)    

    
def start_listen(request, groupname):
    Group.objects.get_or_create(name=groupname)
    cache.set('groupname', groupname)
    
    # default add exist or new added host if start listen
    host_up.connect(join_exist_host, sender=Host)
    post_save.connect(join_new_host, sender=Host)
    
    return HttpResponse('conn')


def stop_listsn(request, groupname):
    host_up.disconnect(join_exist_host, sender=Host)
    post_save.disconnect(join_new_host, sender=Host)
    return HttpResponse('disconn')


