"""Travel Destinations Views"""
from django.shortcuts import render
from django.views import generic
from .models import TravelDestinations


class DestinationsList(generic.ListView):
    """View to display all destinations in the TravelDestinations Model"""
    destinations = TravelDestinations.objects.all()
    queryset = TravelDestinations.objects.filter(
        status=1).order_by('-created_on')
    template_name = 'all_destinations.html'
    paginate_by = 12
