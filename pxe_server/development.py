
from pxe_server.settings import *
DEBUG=True
TEMPLATE_DEBUG=DEBUG

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

INSTALLED_APPS = (
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
    'django.contrib.staticfiles',                  
    'boot',
    'memtest_report',
)