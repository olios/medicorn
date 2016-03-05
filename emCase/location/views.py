from django.shortcuts import render

# Create your views here.

from location.models import Location
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .forms import LocationForm

# Create your views here.
def index_location(request):
    return render(request, 'index_location.html', { })

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def run_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        
        if form.is_valid():
            # RUN devices!
            # from run_devices import ...
            from .models import Location
            _lng = form.cleaned_data["lng"]
            _lat = form.cleaned_data["lat"]
            Location.objects.create(lng=_lng, lat=_lat)
            print("CREATED LOCATION!!!")

            _command = form.cleaned_data["command"]
            from .run_devices  import megafunc
            res = megafunc(_lng, _lat, _command)
            return render(request, 'activated.html', {'log' :  res})
    else:
        form = LocationForm()
    return render(request, 'loc_form.html', {'form' : form})

"""def view_device(request, id_number):
	#id_number = request.GET.get("id_number")
	device = get_object_or_404(Device, id_number=id_number)
	lat = device.location.split(",")[0].strip()
	lng = device.location.split(",")[1].strip()
	return render(request, 'view_device.html', {'device' : device, 'lng': lng, 'lat': lat })	"""

