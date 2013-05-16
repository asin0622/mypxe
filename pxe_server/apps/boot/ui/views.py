from django.shortcuts import render
from boot.models import Host
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from plugins import get_host_actions

def render_index_with_hosts(request, host_list):
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
        
def index(request):
    host_list = Host.objects.all()
    return render_index_with_hosts(request, host_list)


