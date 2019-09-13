from django.urls import path

from . import views

app_name = 'ipanel'

urlpatterns = [
    path('register/', views.register, name='register')
]