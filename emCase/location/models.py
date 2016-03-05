from django.db import models

# Create your models here.
class Location(models.Model):
    
    id_entry = models.IntegerField(unique=True, verbose_name="Log id")
    lng = models.FloatField(verbose_name="Longitude")
    lat = models.FloatField(verbose_name="Latitude")
    timestamp = models.DateTimeField(verbose_name="Time", auto_now_add=True)

