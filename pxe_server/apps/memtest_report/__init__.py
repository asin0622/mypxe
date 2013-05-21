from django.conf import settings
from django.conf.urls import patterns, include
from plugins import app_register
import urls
from boot.models import Host

if "memtest_report" in settings.INSTALLED_APPS:
    app_register.send(sender=None, menu={
        'memtest': { 
            'desc': 'Memtest86',
            'templates': ['memtest_report/templates/action.ipxe']
        }
    })
    
    '''
    extend Host function
    '''
    Host.last_memtest = lambda self: self.results.all()[0].is_good if self.results.count() > 0 else None