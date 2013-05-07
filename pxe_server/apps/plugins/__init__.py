import django.dispatch
from django.dispatch.dispatcher import receiver
from django.conf import settings
import logging

app_register = django.dispatch.Signal(providing_args=["menu"])

MENUITEM = {}

@receiver(app_register)
def reg_app(sender, **kargs):
    logging.info('install app - %s ', kargs['menu'].keys()[0])
    MENUITEM.update(kargs['menu'])

def get_apps():
    return MENUITEM
    