from boot.ui.views import HostList
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from grouping.models import Group


class GroupList(ListView):
    model = Group
    template_object_name = 'group'
    template_name = 'grouping/group_list.html'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(GroupList, self).get_context_data(**kwargs)
        context['listening'] = cache.get('groupname')
        return context


class GroupingHostList(HostList):
    def get_queryset(self):
        self.group = get_object_or_404(Group, name=self.kwargs['groupname'])
        return self.group.hosts.all()
