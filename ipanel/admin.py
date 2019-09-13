from django.contrib import admin

from .models import IPanelAuth, Vote
# Register your models here.
admin.site.register(IPanelAuth)
admin.site.register(Vote)