from urllib.request import urlopen


def get_nearby_devices(lng, lat, type_of_dev, radius=500):
    # TODO

    from device.models import Device
    return Device.objects.filter(type_of_device=type_of_dev)


def toggle_devices(list_of_devs, command):
    check_list = {}
    chk = False
    for device in list_of_devs:
        try:
            urlopen("http://{}:{}/{}".format(device.ip_addrr, device.port, command))
            chk = True
            if command == "start"
                device.status = "Triggered"
            else:
                device.status = "Working"
        except:
            print("NEJAKA CHYBA!")
            chk = False
        check_list[device.human_readable_name] = chk
    return check_list

def megafunc(lng, lat, command):
    cmd, typ = command.split()
    devices = get_nearby_devices(lng, lat, typ)
    d = toggle_devices(devices, cmd)
    return d
