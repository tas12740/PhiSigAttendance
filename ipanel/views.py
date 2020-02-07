from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'ipanel/index.html')

def register(request):
    return render(request, 'ipanel/register.html')


def votes(request):
    return render(request, 'ipanel/vote.html')


def status(request):
    if request.user.is_authenticated:
        username = request.user.username
        if username != 'mediators' and username != 'admin':
                return redirect('/ipanel/vote/')
        return render(request, 'ipanel/status.html')
    return redirect('/ipanel/vote/')


def results(request):
    if request.user.is_authenticated:
        username = request.user.username
        if username != 'mediators' and username != 'admin':
            return redirect('/ipanel/vote/')
        return render(request, 'ipanel/results.html')
    return redirect('/ipanel/vote/')


def generate_status(request):
    if request.user.is_authenticated:
        username = request.user.username
        if username != 'mediators' and username != 'admin':
            return redirect('/ipanel/vote/')
        return render(request, 'ipanel/generate.html')
    return redirect('/ipanel/vote/')
