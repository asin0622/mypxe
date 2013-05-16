from django.shortcuts import render
from memtest_report.models import TestResult
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    result_list = TestResult.objects.all()
    paginator = Paginator(result_list, 10)
    
    page = request.GET.get('page')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
            
    return render(request, 'memtest/index.html', {'results': results})


