from django.shortcuts import redirect, render

def bylaws(request):
    return redirect('https://docs.google.com/document/d/1TJx-mJLdut4cFLzk8EtKMqcs4WqiXoKK3NSrpWfdtPI/edit?usp=sharing')

def sops(request):
    return redirect('https://docs.google.com/document/d/1DnSLWM6Lq1QI_aErXVLyPPAuCsRQVchtiBbGudmFO68/edit?usp=sharing')