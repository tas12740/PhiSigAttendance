from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('hello, world')


def checkin(request, unique_id):
    return HttpResponse(f'Checkin {unique_id}')
