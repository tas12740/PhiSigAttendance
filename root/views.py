from django.shortcuts import render

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
