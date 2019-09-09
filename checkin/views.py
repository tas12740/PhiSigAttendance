from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound, HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest, HttpResponse

from .models import Event, Sibling, CheckIn


def index(request):
    return render(request, 'checkin/index.html')


def checkin(request, unique_id):
    try:
        event = Event.objects.get(unique_id=unique_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound(f'Event with the code {unique_id} does not exist.')

    context = {
        'title': event.name,
        'eventCode': event.unique_id
    }
    return render(request, 'checkin/checkin.html', context)


def register_sibling(request):
    if request.method == 'POST':
        data = request.POST

        onyen = data.get('onyen')

        if onyen is None:
            return HttpResponseBadRequest('You must submit your onyen.')

        if Sibling.objects.filter(onyen=onyen).exists():
            return HttpResponseBadRequest(f'A sibling with the onyen {onyen} already exists.')

        first_name = data.get('first_name')

        if first_name is None:
            return HttpResponseBadRequest('You must submit your first name')

        first_name = first_name.title()

        last_name = data.get('last_name')

        if last_name is None:
            return HttpResponseBadRequest('You must submit your last name.')

        last_name = last_name.title()

        email = data.get('email')

        if email is None:
            return HttpResponseBadRequest('You must submit your email.')

        pledge_class = data.get('pledge_class')

        if pledge_class is None:
            return HttpResponseBadRequest('You must submit your pledge class.')

        pledge_class = pledge_class.title()

        new_sibling = Sibling(first_name=first_name, last_name=last_name,
                              onyen=onyen, email=email, pledge_class=pledge_class)
        try:
            new_sibling.save()
        except Exception as e:
            return HttpResponseBadRequest(f'{e}')

        return HttpResponse(status=201)

    return render(request, 'checkin/register.html')
