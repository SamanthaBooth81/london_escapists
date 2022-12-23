"""Travel destinations app forms"""
from django import forms
from .models import Destinations


class AddDestinationForm(forms.ModelForm):
    """Form for adding a travel destinations"""
    class Meta:
        """Form model and Fields"""
        model = Destinations
        fields = '__all__'
