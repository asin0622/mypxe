from django.conf import settings

if "ubuntu" in settings.INSTALLED_APPS:
    MENUITEM = getattr(settings, 'IPXE_MENUITEM', {})
    MENUITEM['ubuntu'] = { 
        'desc': 'Install Ubuntu 12.04 Server x86_64',
        'templates': ['ubuntu/templates/action.ipxe']
    }