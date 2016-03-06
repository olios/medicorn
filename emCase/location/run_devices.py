from urllib.request import urlopen


def get_nearby_devices(lng, lat, type_of_dev, radius=500):
    # TODO

    from device.models import Device
    if type_of_dev == "all":
        return Device.objects.all()

    return Device.objects.filter(type_of_device=type_of_dev)


def toggle_devices(list_of_devs, command):
    check_list = {}
    id_list = []
    chk = False
    for device in list_of_devs:
        try:
            urlopen("http://{}:{}/{}".format(device.ip_addrr, device.port, command), timeout=0.5)
            id_list.append(device.id_number)
            chk = True
            if command == "start":
                device.status = "Triggered"
            else:
                device.status = "Working"
            device.save()            
        except:
            print("NEJAKA CHYBA!")
            chk = False
        check_list[device.human_readable_name] = chk        
    print(id_list)
    return check_list, list_of_devs

def megafunc(lng, lat, command):
    cmd, typ = command.split()
    devices = get_nearby_devices(lng, lat, typ)
    d, ids = toggle_devices(devices, cmd)
    return d, devices
