from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('findEvent/', views.find_event, name='findEvent'),
    path('checkin/', views.add_checkin, name='checkin'),
    path('recruitmentOnyen/', views.recruitment_onyen, name='recruitmentOnyen'),
    path('pnmCheckIn/', views.pnm_checkin, name='pnmCheckIn'),
    path('ipanelRegister/', views.register_ipanel, name='ipanelRegister'),
    path('ipanelOpens/', views.ipanel_opens, name='ipanelOpens'),
    path('ipanelVote/', views.vote, name='ipanelvote'),
    path('ipanelResults/', views.ipanel_results, name='ipanelResults'),
    path('ipanelStatus/', views.pnm_status, name='ipanelStatus'),
    path('deleteIPanelStatus/', views.delete_status, name='deleteIPanelStatus'),
    path('generateIPanelStatus/', views.generate_status,
         name='generateIPanelStatus')
]
