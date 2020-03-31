from django.urls import path

from . import views

app_name = 'root'

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('documents/', views.documents, name='documents'),
    path('committees/', views.committees, name='committees'),
    path('cons/', views.cons, name='cons'),
    path('consSubmissions/', views.cons_view_all, name='consSubmissions'),
    path('box/', views.box, name='box')
]
