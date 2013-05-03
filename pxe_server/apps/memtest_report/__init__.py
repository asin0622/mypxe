from django.conf import settings
from django.conf.urls import patterns, include
import urls

if "memtest_report" in settings.INSTALLED_APPS:
    MENUITEM = getattr(settings, 'IPXE_MENUITEM', {})
    MENUITEM['memtest'] = { 
        'desc': 'Memtest86',
        'templates': ['memtest_report/templates/action.ipxe']
    }