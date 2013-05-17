from boot.models import Host
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from plugins import get_host_actions


class HostDetail(DetailView):
    model = Host
    template_name = 'boot/host_detail.html'
    slug_field = '_mac'
    slug_url_kwarg = 'mac'

class HostList(ListView):
    model = Host
    template_object_name = 'host'
    template_name = 'boot/host_list.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(HostList, self).get_context_data(**kwargs)
        context['total_count'] = Host.objects.count()
        context['actions'] = get_host_actions()
        return context


