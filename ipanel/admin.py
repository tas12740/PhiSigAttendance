from django.contrib import admin

from .models import IPanelAuth, Vote, PNMIPanel
# Register your models here.
admin.site.register(IPanelAuth)
admin.site.register(Vote)
admin.site.register(PNMIPanel)