from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from root.models import Box, ConsSubmission

from django.templatetags.static import static
from django.conf import settings


def cons(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    url = static('root/data/cons.json')

    onyen = request.POST.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest("You must submit your onyen")

    new_con_row = ConsSubmission(onyen=onyen)
    try:
        new_con_row.save()
    except:
        return HttpResponseBadRequest('Unexpected failure!')

    host = 'http' if settings.DEBUG else 'https'
    response = get(f'{host}://{request.get_host()}{url}')

    json = response.json()

    restricted = json['restricted'][onyen] if onyen in json['restricted'] else []
    can_see = [cat for cat in json['cons'] if cat not in restricted]

    map_positions = {
        'pres': 'President',
        'vp': 'Vice President',
        'parlia': 'Parliamentarian',
        'rec-sec': 'Recording Secretary',
        'corr-sec': 'Corresponding Secretary',
        'treasurer': 'Treasurer',
        'historian': 'Historian',
        'ias': 'Initiate Advisors',
        'mediators': 'Mediators',
        'scholarship': 'Scholarship',
        'fellowship': 'Fellowship',
        'service': 'Service',
        'recruitment': 'Recruitment',
        'pr': 'Public Relations (PR)',
        'fundraising': 'Fundraising',
        'alumni': 'Alumni',
        'it': 'Information Technology (IT)',
        'im/rec': 'IM/Recreation',
        'ip': 'Intentional Programming (IP)',
        'icr': 'Interchapter Relations (ICR)',
        'standards': 'Standards'
    }

    res = dict()
    for pos in can_see:
        res[map_positions[pos]] = json['cons'][pos]

    return JsonResponse(res)


def box(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    submission = request.POST.get('submission')
    if submission is None:
        return HttpResponseBadRequest("You must submit something, silly!")

    new_box_row = Box(submission=submission)
    try:
        new_box_row.save()
    except:
        return HttpResponseBadRequest('Unexpected failure!')

    return JsonResponse({'success': True})
