from django.urls import path

from . import views

app_name = 'ipanel'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('vote/', views.votes, name='vote'),
    path('results/', views.results, name='results'),
    path('status/', views.status, name='status'),
    path('generate/', views.generate_status, name='generateStatus')
]