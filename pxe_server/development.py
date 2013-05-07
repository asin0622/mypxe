
from pxe_server.settings import *
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

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'gunicorn',                      
    'memtest_report',
    'ubuntu',
    'boot',
    'plugins'
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "apps"),
    os.path.join(os.path.dirname(__file__), "templates"),
)

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