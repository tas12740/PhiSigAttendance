from django.urls import path

from . import views

app_name = 'recruitment'

urlpatterns = [
    path('checkin/', views.checkin, name='checkin'),
    path('emails/', views.emails, name='emails')
]
