from django.shortcuts import render, HttpResponse
from device.models import Device

# Create your views here.
def index(request):
    return render(request, 'index.html', {'devices' : Device.objects.all(), 'test': "QWERTYUIOP"})

def view_device(request, id_number):
	return render(request, 'index.html', {'devices' : Device.objects.filter(id_number=id_number), 'test': id_number })	
    
