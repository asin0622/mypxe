from boot.models import Host
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
import django.dispatch
import logging

host_action = Signal(providing_args=["action"])
host_event = Signal(providing_args=['message'])

@receiver(host_action)
def change_host_next_action(sender, **kargs):
    logging.info('%s - default action = %s' % (sender, kargs['action'])) 
    sender.set_default_action(kargs['action'])