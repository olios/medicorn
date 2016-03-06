from django.shortcuts import render, HttpResponse
from device.models import Device
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {'devices' : Device.objects.all(), 'test': "QWERTYUIOP"})

def view_device(request, id_number):
    #id_number = request.GET.get("id_number")
    device = get_object_or_404(Device, id_number=id_number)
    lat = device.location.split(",")[0].strip()
    lng = device.location.split(",")[1].strip()
    return render(request, 'view_device.html', {'device' : device, 'lng': lng, 'lat': lat })	
    
def visualization(request):

    from device.models import Device
    from django.db.models import Count
    counts = [((val["type_of_device"], val["type_of_device__count"])) for val in Device.objects.values("type_of_device").annotate(Count("type_of_device"))]

    r = get_plots(counts)
    import plotly.tools as tls

    bar = tls.get_embed(r)
    return render(request, 'visual.html', {"type": bar })

def get_plots(counts):
    import plotly.plotly as py
    import plotly.graph_objs as go
    import plotly.tools as tls
    py.sign_in('kotrfa', 'etp2llol2i') 
    # (1) Two lists of numbers
    print(counts)

    x1 = [x for x,y in counts]
    y1 = [y for x,y in counts]

    data = [go.Bar(x=x1, y=y1)]
    
    layout = go.Layout(
        title='Type of device',
    )

    return py.plot(data, filename='type of device', auto_open=False)

