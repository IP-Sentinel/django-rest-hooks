import django
from django.dispatch import Signal


if django.VERSION >= (4, 0,):
    hook_event = Signal() # providing_args=['action', 'instance']
    raw_hook_event = Signal() # providing_args=['event_name', 'payload', 'user']
    hook_sent_event = Signal() # providing_args=['payload', 'instance', 'hook']
else:
    hook_event = Signal(providing_args=['action', 'instance'])
    raw_hook_event = Signal(providing_args=['event_name', 'payload', 'user'])
    hook_sent_event = Signal(providing_args=['payload', 'instance', 'hook'])
