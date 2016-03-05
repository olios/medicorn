from django import forms

class LocationForm(forms.Form):
    lng = forms.FloatField(label="Longitude")
    lat = forms.FloatField(label="Latitude")
