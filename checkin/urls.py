from django.urls import path

from . import views

app_name = 'checkin'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:unique_id>/', views.checkin, name='checkin'),
    path('api/findEvent/', views.find_event, name='findEvent'),
    path('api/checkin/', views.add_checkin, name='handleCheckIn'),
    path('register/sibling/', views.register_sibling, name='registerSibling')
]
