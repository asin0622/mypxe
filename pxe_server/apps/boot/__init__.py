from boot.models import Host
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
import django.dispatch
import logging

host_up = Signal(providing_args=['instance', 'created'])
host_event = Signal(providing_args=['message', 'action'])

@receiver(host_event)
def host_event_receiver(sender, message=None, action=None, **kargs):
    if message is not None:
        logging.info('%s - %s' % (sender, message))
    if action is not None:
        logging.info('%s - default action = %s' % (sender, action)) 
        sender.set_default_action(action)