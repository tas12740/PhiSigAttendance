from django.shortcuts import render

# Create your views here.
def checkin(request):
    return render(request, 'recruitment/checkin.html')