import os
import sys

sys.path = ['/home/www/pxe/', '/home/www/pxe/pxe_server/apps'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'pxe_server.development'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
