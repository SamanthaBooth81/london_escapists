from django.contrib import admin
from .models import TravelDestinations


class TravelDestinationAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'destination',
        'created_on',
        'updated_on',
        'top_destination',
        'status',
    )


admin.site.register(TravelDestinations, TravelDestinationAdmin)