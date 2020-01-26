from django.shortcuts import render

# Create your views here.


def documents(request):
    return render(request, 'siblings/documents.html')
