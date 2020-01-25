from django.urls import path

from . import views

app_name = 'root'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus')
]
