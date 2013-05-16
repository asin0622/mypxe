from django.conf import settings
from plugins import app_register

if "ubuntu" in settings.INSTALLED_APPS:
    app_register.send(sender=None, menu={
        'ubuntu': { 
            'desc': 'Install Ubuntu 12.04 Server x86_64',
            'templates': ['ubuntu/templates/action.ipxe']
        }
    })