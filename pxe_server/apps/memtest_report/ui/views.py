from django.shortcuts import render
from memtest_report.models import TestResult
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import ListView

def index(request):
    result_list = TestResult.objects.order_by('-end_datetime', '-start_datetime')
    paginator = Paginator(result_list, 10)
    
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
            
    return render(request, 'memtest/index.html', {'results': results})


class MemtestResultList(ListView):
    model = TestResult
    paginate_by = 10
    context_object_name = 'result_list'
    template_name = 'memtest/result_list.html'