from django.db import models

# Create your models here.

class Device(models.Model):
    type_choice = (
            ("FD", "Fire Distinguisher"),
            ("MK", "Medi Kit"),
            ("FB", "Fuse box"),
            ("O", "Other")
            )

    status_choice = (
            ("Working", "Working"),
            ("Problem", "Problem"),
            ("Broken", "Broken"),
            ("Triggered", "Triggered"),
            ("Other", "Other")
            )

    id_number = models.IntegerField(unique=True, verbose_name="Serial Number of IoT")
    human_readable_name = models.CharField(max_length=100, verbose_name="Human readable name")
    insert_date = models.DateTimeField(verbose_name="Insert Date")
    type_of_device = models.CharField(max_length=100, choices=type_choice, verbose_name="Type of a device")
    last_check_date = models.DateTimeField(verbose_name="Last Check date")
    location = models.CharField(max_length=100, verbose_name="GPS Location")
    description_of_device = models.TextField(verbose_name = "Description of a device")
    description_of_content = models.TextField(verbose_name = "Description of a content")
    status = models.CharField(max_length=100, choices=status_choice, verbose_name = "Status")
    posted = models.BooleanField(default=False, verbose_name="Posted")
    ip_addrr = models.GenericIPAddressField(blank=False, verbose_name="IP addrres")
    port = models.IntegerField(verbose_name="Port")

    
