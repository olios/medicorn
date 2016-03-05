from urllib.request import urlopen


def get_nearby_devices(lng, lat, type_of_dev, radius=500):
    # TODO

    from device.models import Device
    return Device.objects.all()


def toggle_devices(list_of_devs, command):
    check_list = {}
    chk = False
    for device in list_of_devs:
        try:
            urlopen("http://{}:{}/{}".format(device.ip_addrr, device.port, command))
            chk = True
        except:
            print("NEJAKA CHYBA!")
            chk = False
            raise
        check_list[device.id] = chk
    return check_list

def megafunc(lng, lat, command):
    devices = get_nearby_devices(lng, lat)
    d = toggle_devices(devices, command)
    return d
