from django.shortcuts import render

from root.models import ConsSubmission

# Create your views here.


def index(request):
    return render(request, 'root/index.html')


def aboutus(request):
    return render(request, 'root/aboutus.html')


def contact(request):
    return render(request, 'root/contact.html')


def documents(request):
    return render(request, 'root/documents.html')


def committees(request):
    return render(request, 'root/committees.html')


def cons(request):
    return render(request, 'root/cons.html')


def cons_view_all(request):
    onyens = ConsSubmission.objects.all()
    return render(request, 'root/viewcons.html', context={'onyens': onyens})


def box(request):
    return render(request, 'root/box.html')


def letter(request):
    return render(request, 'root/letter.html')


def goodbye(request):
    return render(request, 'root/2020goodbye.html')
