from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from grouping.models import Group
from django.core.cache import cache
from plugins import get_host_actions

def index(request):
    group_list = Group.objects.all()
    paginator = Paginator(group_list, 10)
    
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    
    current_listen_group = cache.get('groupname')
    return render(request, 'grouping/index.html', {'groups': groups, 'listening': current_listen_group})


def hosts_in_group(request, groupname):
    group = Group.objects.get(name=groupname)
    host_list = group.hosts.all()
    paginator = Paginator(host_list, 10)
    
    page = request.GET.get('page')
    try:
        hosts = paginator.page(page)
    except PageNotAnInteger:
        hosts = paginator.page(1)
    except EmptyPage:
        hosts = paginator.page(paginator.num_pages)
    
    actions = get_host_actions()
    return render(request, 'boot/index.html', {'hosts': hosts, 'actions': actions, 'total_count': host_list.count()})


