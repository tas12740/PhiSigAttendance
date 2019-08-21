from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed, JsonResponse

from .models import Event

# Create your views here.


def index(request):
    return render(request, 'checkin/index.html')


def checkin(request, unique_id):
    try:
        event = Event.objects.get(unique_id=unique_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound(f'Event with the code {unique_id} does not exist.')

    context = {
        'title': event.name
    }
    return render(request, 'checkin/checkin.html', context)


def find_event(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    unique_id = request.POST['unique_id']
    try:
        Event.objects.get(unique_id=unique_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound(f'Event with the code {unique_id} does not exist.')

    return JsonResponse({
        'url': reverse('checkin:checkin', kwargs={'unique_id': unique_id})
    })
