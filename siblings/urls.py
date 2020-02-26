from django.urls import path

from . import views

app_name = 'siblings'

urlpatterns = [
    path('documents/', views.documents, name='documents'),
    path('links/', views.documents, name='links')
]
