from urllib.request import urlopen


def get_nearby_devices(radius=500):
    pass


def toggle_devices(list_of_devs, command):
    for device in list_of_devs:
        try:
            urlopen("http://{}:{}/{}".format(device.ip_addr, device.port)
        except as ex:
            print("NEJAKA CHYBA!")
