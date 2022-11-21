"""Travel Destinations Views"""
from django.shortcuts import render
from .models import TravelDestinations


def all_destinations(request):
    """View to display all destinations in the TravelDestinations Model"""
    destinations_list = TravelDestinations.objects.filter(
        status=1).order_by('-created_on')
    template = 'all_destinations.html'
    paginate_by = 12
    context = {
        'destinations_list': destinations_list,
    }
    return render(request, template, context)
