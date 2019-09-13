from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('findEvent/', views.find_event, name='findEvent'),
    path('checkin/', views.add_checkin, name='checkin'),
    path('recruitmentOnyen/', views.recruitment_onyen, name='recruitmentOnyen'),
    path('pnmCheckIn/', views.pnm_checkin, name='pnmCheckIn'),
    path('ipanelRegister/', views.register_ipanel, name='ipanelRegister')
]