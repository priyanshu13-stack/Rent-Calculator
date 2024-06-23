from django import forms
from .models import RentEntry

class RentForm(forms.ModelForm):
    last_electricity_units = forms.IntegerField(label='Last Month Electricity Units', required=False, widget=forms.NumberInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = RentEntry
        fields = ['monthly_rent', 'last_electricity_units', 'current_electricity_units', 'cost_per_unit']
