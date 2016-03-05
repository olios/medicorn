from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('human_readable_name', 'type_of_device', 'posted' )

admin.site.register(Device, DeviceAdmin)
