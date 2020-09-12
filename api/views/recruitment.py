from django.http import HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse

from recruitment.models import PNM


def checkin_type(event_name, event_type):
    if 'Potluck' in event_type:
        return {
            'potluck': 1
        }
    if 'Friday' in event_type:
        return {
            'open_friday': 1
        }
    try:
        event_type_obj = EventType.objects.get(name=event_type)
    except EventType.DoesNotExist:
        return False

    if 'First' in event_type:
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
            event_type=event_type_obj).order_by('date_time')
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
        return HttpResponseNotFound()

    # we know that the PNM is in the database
    event_type = request.POST.get('event_type')
    if event_type is None:
        return HttpResponseBadRequest('You must submit the event type.')

    event_name = request.POST.get('event_name')
    if event_name is None:
        return HttpResponseBadRequest('You must submit the event name.')

    kwargs = checkin_type(event_name, event_type)
    if not kwargs:
        return HttpResponseBadRequest('Failed to find a valid event for this submission.')

    try:
        # we expect a dictionary so try to get the first key and value
        attrib = list(kwargs.keys())[0]
        val = list(kwargs.values())[0]
        setattr(pnm_checkin, attrib, val)
        pnm_checkin.save()
    except Exception as e:
        print(e)
        return HttpResponse(status=500)

    return JsonResponse({
        'name': f'{pnm_checkin.first_name} {pnm_checkin.last_name}'
    })


def pnm_checkin(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

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
