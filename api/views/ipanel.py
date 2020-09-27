from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponseBadRequest, HttpResponse

from requests import get
from string import ascii_lowercase
from random import choice

from ipanel.models import IPanelAuth, Vote, PNMIPanel

nums = list(range(0, 10))
nums = [str(x) for x in nums]
nums = ''.join(nums)
choices = ascii_lowercase + nums


def register_ipanel(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    data = request.POST

    onyen = data.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest('You must submit the onyen.')

    if (auth := IPanelAuth.objects.filter(onyen=onyen)).exists():
        return JsonResponse({
            'code': auth.passcode
        }, status=400)

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


def ipanel_opens(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_methods=['GET'])

    opens = PNMIPanel.objects.filter(status=PNMIPanel.OPEN)

    opens = [pnm.number for pnm in opens]

    return JsonResponse({
        'pnms': opens
    })


def vote(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    data = request.POST

    onyen = data.get('onyen')
    if onyen is None:
        return HttpResponseBadRequest('You must submit your onyen.')

    code = data.get('code')
    if data is None:
        return HttpResponseBadRequest('You must submit your passcode.')

    try:
        ipanel_voter = IPanelAuth.objects.get(onyen=onyen)
    except IPanelAuth.DoesNotExist:
        return HttpResponseBadRequest('You need to register!')

    if code != ipanel_voter.passcode:
        return HttpResponseBadRequest('You entered the wrong passcode.')

    success_pnms = []
    error_pnms = []
    error_statuses = []
    for key, value in data.items():
        if key == 'onyen' or key == 'code' or key == 'csrfmiddlewaretoken':
            continue

        if Vote.objects.filter(vote_onyen=ipanel_voter, pnm_number=key).exists():
            error_pnms.append(key)
            error_statuses.append(f'You already voted on PNM {key}')
            continue

        try:
            pnm_status = PNMIPanel.objects.get(number=key)
        except PNMIPanel.DoesNotExist:
            error_pnms.append(key)
            error_statuses.append(f'PNM {key} has not been set up')
            continue

        if pnm_status.status == PNMIPanel.LOCKED:
            error_pnms.append(key)
            error_statuses.append(f'PNM {key} is locked')
            continue

        new_vote = Vote(vote_onyen=ipanel_voter, pnm_number=key, vote=value)

        try:
            new_vote.save()
            success_pnms.append(key)
        except:
            return HttpResponseBadRequest(f'Vote failed for PNM {key}. Try again or contact an admin.')

    return JsonResponse({
        'success_pnms': success_pnms,
        'error_pnms': error_pnms,
        'error_statuses': error_statuses
    })


def ipanel_results(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    cutoff = request.POST.get('cutoff')

    try:
        cutoff = int(cutoff) / 100
    except Exception as e:
        return HttpResponseBadRequest(e)

    try:
        pnms = Vote.objects.order_by().values_list('pnm_number', flat=True).distinct()
    except Exception as e:
        return HttpResponseBadRequest(e)

    results = dict()

    for pnm in pnms:
        try:
            yes = Vote.objects.filter(pnm_number=pnm, vote=Vote.YES).count()
            no = Vote.objects.filter(pnm_number=pnm, vote=Vote.NO).count()
        except Exception as e:
            return HttpResponseBadRequest(e)

        if yes + no == 0:
            continue

        percent = yes / (yes + no)

        result = percent >= cutoff

        percent = percent * 100
        results[pnm] = ['Yes', percent] if result else ['No', percent]

    return JsonResponse(results)


def pnm_status(request):
    if request.method not in ['GET', 'POST', 'DELETE', 'PUT']:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST', 'DELETE', 'PUT'])

    if request.method == 'DELETE':
        return delete_status(request)
    elif request.method == 'POST':
        return generate_status(request)

    if request.method == 'PUT':
        success_pnms = []
        error_pnms = []
        # post list of number, status
        for key in request.data:
            if key == 'csrfmiddlewaretoken':
                continue

            try:
                pnm_status_obj = PNMIPanel.objects.get(number=key)
            except PNMIPanel.DoesNotExist:
                error_pnms.append(key)
                continue

            status = PNMIPanel.LOCKED if request.data[key] == 'L' else PNMIPanel.OPEN

            if status == pnm_status_obj.status:
                continue

            pnm_status_obj.status = status
            try:
                pnm_status_obj.save()
                success_pnms.append(key)
            except:
                error_pnms.append(key)
                continue

        return JsonResponse({
            'success_pnms': success_pnms,
            'error_pnms': error_pnms
        })

    pnms = PNMIPanel.objects.all()
    result = dict()
    result = {pnm.number: pnm.status for pnm in pnms}

    return JsonResponse(result)


def delete_status(request):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed(permitted_methods=['DELETE'])

    try:
        PNMIPanel.objects.all().delete()
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponseBadRequest(e)


def generate_status(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    start = request.POST.get('start')
    if start is None:
        return HttpResponseBadRequest('You must submit a start to the range.')
    try:
        start = int(start)
    except Exception as e:
        return HttpResponseBadRequest(e)

    end = request.POST.get('end')
    if end is None:
        return HttpResponseBadRequest('You must submit an end to the range.')
    try:
        end = int(end)
    except Exception as e:
        return HttpResponseBadRequest(e)

    if end < start:
        return HttpResponseBadRequest('Start must be less than or equal to the end.')

    failed = []
    for num in range(start, end+1):
        new_pnm_status = PNMIPanel(number=num, status=PNMIPanel.LOCKED)

        try:
            new_pnm_status.save()
        except:
            failed.append(num)
            continue

    return JsonResponse({
        'failed': failed
    })
