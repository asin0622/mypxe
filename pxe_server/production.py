
from pxe_server.settings import *

STATIC_URL = 'http://192.168.22.1/static/'
STATIC_ROOT = '/tmp/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.sqlite',
    }
}

INSTALLED_APPS = (
    'django.contrib.staticfiles',                  
    'boot',
    'memtest_report',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "apps"),
    os.path.join(os.path.dirname(__file__), "templates"),
)

IPXE_MENUITEM = {}