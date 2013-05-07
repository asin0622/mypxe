from django.conf import settings
from django.conf.urls import patterns, include
from plugins import app_register
import urls

if "memtest_report" in settings.INSTALLED_APPS:
    app_register.send(sender=None, menu={
        'memtest': { 
            'desc': 'Memtest86',
            'templates': ['memtest_report/templates/action.ipxe']
        }
    })