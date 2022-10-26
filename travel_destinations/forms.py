"""Travel destinations app forms"""
from django import forms
from .models import TravelDestinations


class AddDestinationForm(forms.ModelForm):
    """Form for adding a travel destinations"""
    class Meta:
        """Form model and Fields"""
        model = TravelDestinations
        fields = '__all__'
