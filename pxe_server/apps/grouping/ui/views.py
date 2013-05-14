from boot.ui.views import render_index_with_hosts
from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from grouping.models import Group

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
    return render_index_with_hosts(request, host_list)


