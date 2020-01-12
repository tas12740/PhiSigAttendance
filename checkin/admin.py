from django.contrib import admin

from .models import Sibling, Event, EventType, GPATracker, CheckIn, Alumni
# Register your models here.
admin.site.register(Sibling)
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(GPATracker)
admin.site.register(CheckIn)
admin.site.register(Alumni)
