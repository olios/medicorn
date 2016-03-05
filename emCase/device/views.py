from django.shortcuts import render, HttpResponse
from device.models import Device

# Create your views here.
def index(request):
    return render(request, 'index.html', {'devices' : Device.objects.all()})

# def device(request):
#    
