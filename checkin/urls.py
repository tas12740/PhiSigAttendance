from django.urls import path

from . import views

app_name = 'checkin'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:unique_id>/', views.checkin, name='checkin'),
    path('register/sibling/', views.register_sibling, name='registerSibling')
]
