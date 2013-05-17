
from pxe_server.settings import *
import tempfile

DEBUG=True
TEMPLATE_DEBUG=DEBUG

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ['localhost']

MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    'debug_toolbar',
    # global
    'django.contrib.staticfiles',
    'gunicorn',
    'bootstrap-pagination',
    # apps
    'memtest_report',
    'ubuntu',
    'boot',
    'plugins',
    'grouping',
    'console',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 3600,  # an hour
    }
}

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "apps"),
    os.path.join(os.path.dirname(__file__), "templates"),
)

for app in INSTALLED_APPS:
    TEMPLATE_DIRS += (os.path.join(os.path.dirname(__file__), "apps", app, "templates")), 

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = tempfile.gettempdir()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
         }
    },
    'formatters': {
        'standard': {
            'format' : "%(asctime)s [%(process)d] [%(levelname)s] [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'console':{
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'null': {
            'class':'django.utils.log.NullHandler',
        },                 
        'mail_admins': {
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        '': {
            'handlers':['console'],
            'propagate': False,
            'level':'INFO',
        },
        'gunicorn.error': {
            'level': 'ERROR',
            'handlers': ['null'],
            'propagate': False,
        },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['null'],
            'propagate': False,
        },                
    }
}