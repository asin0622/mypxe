from boot.models import Host
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
import django.dispatch
import logging
from django.core.cache import get_cache

cache = get_cache('host')

host_up = Signal(providing_args=['instance', 'created'])
host_event = Signal(providing_args=['message', 'action'])

@receiver(host_event)
def host_event_receiver(sender, message=None, action=None, **kargs):
    if message is not None:
        msg = '%s - %s' % (sender, message)
    elif action is not None:
        msg = '%s - default action = %s' % (sender, action)
    if action is not None:        
        sender.set_default_action(action)
        
    cache.set(sender.mac, msg)
    logging.info(msg) 