from django.shortcuts import reverse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse

from datetime import date

from checkin.models import Event, Sibling, CheckIn, EventType


def find_event(request):
    if request.method != 'POST' and request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['POST', 'GET'])

    if request.method == 'GET':
        recruitment = request.GET.get('recruitment')
        if recruitment:
            events_today = Event.objects.filter(date_time__date=date.today())
            if len(events_today) == 0:
                return HttpResponseBadRequest('No events were found for today!')
            for eve in events_today:
                if 'Recruitment' in eve.event_type.name or 'Potluck' in eve.event_type.name:
                    return JsonResponse({
                        'eventName': eve.name,
                        'eventType': eve.event_type.name
                    })
            return HttpResponseBadRequest('No recruitment events were found for today!')

    unique_id = request.POST.get('unique_id')
    if not unique_id:
        return HttpResponseBadRequest('You failed to submit a unique ID for the event!')
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
