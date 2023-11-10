from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'location', 'open_time', 'close_time', 'coffee_rating', 'wifi_rating', 'power_outlets']