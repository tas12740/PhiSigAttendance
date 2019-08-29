from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('findEvent/', views.find_event, name='findEvent'),
    path('checkin/', views.add_checkin, name='checkin')
]