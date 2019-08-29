from django.shortcuts import render, reverse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse

from checkin.models import Event, Sibling, CheckIn


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


def add_checkin(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    data = request.POST

    onyen = data.get('onyen')

    if onyen is None:
        return HttpResponseBadRequest('You are required to submit the onyen field.')

    try:
        sibling = Sibling.objects.get(onyen=onyen)
    except Sibling.DoesNotExist:
        return HttpResponseBadRequest(f'A sibling with onyen {onyen} does not exist.')

    event_code = data.get('event_code')

    if event_code is None:
        return HttpResponseBadRequest('You are required to submit the event code.')

    try:
        event = Event.objects.get(unique_id=event_code)
    except Event.DoesNotExist:
        return HttpResponseBadRequest(f'An event with code {event_code} does not exist.')

    if CheckIn.objects.filter(sibling=sibling, event=event).exists():
        return HttpResponseBadRequest(f'{sibling.first_name} {sibling.last_name} has already checked into {event.name}.')

    new_checkin = CheckIn(sibling=sibling, event=event)
    new_checkin.save()

    return HttpResponse(status=201)
