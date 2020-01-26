from django.urls import path

from . import views

app_name = 'siblings'

urlpatterns = [
    path('documents/', views.documents, name='documents')
]
