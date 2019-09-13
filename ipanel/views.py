from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'ipanel/register.html')

def votes(request):
    return render(request, 'ipanel/vote.html')

def results(request):
    return render(request, 'ipanel/results.html')