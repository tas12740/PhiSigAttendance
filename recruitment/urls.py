from django.urls import path

from . import views

app_name = 'recruitment'

urlpatterns = [
    path('checkin/', views.checkin, name='checkin'),
    path('emails/', views.emails, name='emails'),
    path('about/', views.about, name='about'),
    path('requirements/', views.requirements, name='requirements')
]
