from django.conf import settings

MENUITEM = getattr(settings, 'IPXE_MENUITEM', {})
MENUITEM['memtest'] = { 
    'desc': 'Memtest86',
    'templates': ['memtest_report/templates/action.ipxe']
}