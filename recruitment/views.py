from django.shortcuts import render
from django.http import HttpResponse

from .models import PNM

# Create your views here.


def checkin(request):
    return render(request, 'recruitment/checkin.html')


def emails(request):
    pnms = PNM.objects.all()

    emails = []
    for new_pnm in pnms:
        emails.append(new_pnm.email)

    return HttpResponse(','.join(emails))


def about(request):
    return render(request, 'recruitment/about.html')


def requirements(request):
    return render(request, 'recruitment/requirements.html')


def schedule(request):
    return render(request, 'recruitment/schedule.html')


def forms(request):
    return render(request, 'recruitment/forms.html')
