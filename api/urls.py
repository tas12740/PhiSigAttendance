from django.urls import path

from .views import checkin, ipanel, recruitment, spring20

app_name = 'api'

urlpatterns = [
    path('event/', checkin.find_event, name='findEvent'),
    path('checkin/', checkin.add_checkin, name='checkin'),
    path('recruitment/onyen/', recruitment.recruitment_onyen,
         name='recruitmentOnyen'),
    path('recruitment/checkin/', recruitment.pnm_checkin, name='pnmCheckIn'),
    path('ipanel/registration/', ipanel.register_ipanel, name='ipanelRegister'),
    path('ipanel/pnm/open/', ipanel.ipanel_opens, name='ipanelOpens'),
    path('ipanel/vote/', ipanel.vote, name='ipanelvote'),
    path('ipanel/results/', ipanel.ipanel_results, name='ipanelResults'),
    path('ipanel/status/', ipanel.pnm_status, name='ipanelStatus'),
    path('cons/', spring20.cons, name='cons'),
    path('box/', spring20.box, name='box')
]
