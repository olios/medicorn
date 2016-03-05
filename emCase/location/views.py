from django.shortcuts import render

# Create your views here.

from location.models import Location
from django.shortcuts import get_object_or_404

# Create your views here.
def index_location(request):
    return render(request, 'index_location.html', { })

"""def view_device(request, id_number):
	#id_number = request.GET.get("id_number")
	device = get_object_or_404(Device, id_number=id_number)
	lat = device.location.split(",")[0].strip()
	lng = device.location.split(",")[1].strip()
	return render(request, 'view_device.html', {'device' : device, 'lng': lng, 'lat': lat })	"""

