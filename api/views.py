from django.shortcuts import render, reverse
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse

from checkin.models import Event, Sibling, CheckIn, EventType
from recruitment.models import PNM
from ipanel.models import IPanelAuth, Vote

import datetime
from string import ascii_lowercase
from random import choice


def find_event(request):
    if request.method != 'POST' and request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['POST', 'GET'])

    if request.method == 'GET':
        recruitment = request.GET.get('recruitment')
        if recruitment:
            events_today = Event.objects.filter(
                date_time__date=datetime.date.today())
            if len(events_today) == 0:
                return HttpResponseBadRequest('No events were found for today!')
            for eve in events_today:
                if 'Recruitment' in eve.event_type.name or 'Potluck' in eve.event_type.name:
                    return JsonResponse({
                        'eventName': eve.name,
                        'eventType': eve.event_type.name
                    })
            return HttpResponseBadRequest('No recruitment events were found for today!')

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


def checkin_type(event_name, event_type):
    if 'Potluck' in event_type:
        return {
            'potluck': 1
        }
    if 'Friday' in event_type:
        return {
            'open_friday': 1
        }
    if 'First' in event_type:
        event_type_obj = EventType.objects.get(name=event_type)
        events = Event.objects.filter(
            event_type=event_type_obj).order_by('date_time')
        for ind, eve in enumerate(events):
            if event_name == eve.name:
                if ind == 0:
                    return {
                        'open_one': 1
                    }
                elif ind == 1:
                    return {
                        'open_two': 1
                    }
                elif ind == 2:
                    return {
                        'open_three': 1
                    }
        return False
    if 'Second' in event_type:
        events = Event.objects.filter(
            event_type=event_type).order_by('date_time')
        for ind, eve in enumerate(events):
            if event_name == eve.name:
                if ind == 0:
                    return {
                        'closed_one': 1
                    }
                elif ind == 1:
                    return {
                        'closed_two': 1
                    }
                elif ind == 2:
                    return {
                        'closed_three': 1
                    }
        return False
    return False


def recruitment_onyen(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    data = request.POST

    onyen = data.get('onyen')

    if onyen is None:
        return HttpResponseBadRequest('You are required to submit the onyen field.')

    try:
        pnm_checkin = PNM.objects.get(onyen=onyen)
    except PNM.DoesNotExist:
        return HttpResponse(status=400)

    # we know that the PNM is in the database
    event_type = request.POST.get('event_type')
    if event_type is None:
        return HttpResponseBadRequest('You must submit the event type.')

    event_name = request.POST.get('event_name')
    if event_name is None:
        return HttpResponseBadRequest('You must submit the event name.')

    kwargs = checkin_type(event_name, event_type)

    try:
        setattr(pnm_checkin, list(kwargs.keys())[0], list(kwargs.values())[0])
        pnm_checkin.save()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)

    return JsonResponse({
        'name': f'{pnm_checkin.first_name} {pnm_checkin.last_name}'
    })


def pnm_checkin(request):
    event_type = request.POST.get('event_type')
    if event_type is None:
        return HttpResponseBadRequest('You must submit the event type.')

    event_name = request.POST.get('event_name')
    if event_name is None:
        return HttpResponseBadRequest('You must submit the event name.')

    kwargs = checkin_type(event_name, event_type)

    onyen = request.POST.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest('You must submit the onyen.')

    first_name = request.POST.get('first_name')
    if first_name is None:
        return HttpResponseBadRequest('You must submit the first name.')

    last_name = request.POST.get('last_name')
    if last_name is None:
        return HttpResponseBadRequest('You must submit the last name.')

    email = request.POST.get('email')
    if email is None:
        return HttpResponseBadRequest('You must submit the email')

    new_pnm = PNM(onyen=onyen, first_name=first_name,
                  last_name=last_name, email=email, **kwargs)
    try:
        new_pnm.save()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)

    return HttpResponse(status=201)


def register_ipanel(request):
    data = request.POST

    onyen = data.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest('You must submit the onyen.')

    if IPanelAuth.objects.filter(onyen=onyen).exists():
        return HttpResponseBadRequest('You have already checked in to this I Panel. Please contact your friendly admin to get your code.')

    nums = list(range(0, 10))
    nums = [str(x) for x in nums]
    nums = ''.join(nums)
    choices = ascii_lowercase + nums
    code = ''.join(choice(choices) for _ in range(4))

    while IPanelAuth.objects.filter(passcode=code).exists():
        code = ''.join(choice(choices) for _ in range(4))

    new_ipanel_registration = IPanelAuth(onyen=onyen, passcode=code)

    try:
        new_ipanel_registration.save()
    except:
        return HttpResponse(status=500)

    return JsonResponse({
        'code': code
    })

def vote(request):
    data = request.POST

    onyen = data.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest('You must submit the onyen.')

    code = data.get('code')
    if data is None:
        return HttpResponseBadRequest('You must submit your passcode.')
    
    ipanel_voter = IPanelAuth.objects.get(onyen=onyen)

    if code != ipanel_voter.passcode:
        return HttpResponseBadRequest('You entered the wrong passcode.')

    for key, value in data.items():
        if key == 'onyen' or key == 'code' or key == 'csrfmiddlewaretoken': 
            continue

        if Vote.objects.filter(vote_onyen=ipanel_voter, pnm_number=key).exists():
            continue

        new_vote = Vote(vote_onyen = ipanel_voter, pnm_number=key, vote=value)

        try:
            new_vote.save()
        except:
            return HttpResponseBadRequest(f'Vote failed for PNM {key}. Try again or contact an admin.')

    return HttpResponse(status=201)
    