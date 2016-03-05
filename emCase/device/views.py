from django.shortcuts import render, HttpResponse
from device.models import Device
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {'devices' : Device.objects.all(), 'test': "QWERTYUIOP"})

def view_device(request, id_number):
	#id_number = request.GET.get("id_number")
	return render(request, 'view_device.html', {'device' : get_object_or_404(Device, id_number=id_number), 'test': id_number })	
    
