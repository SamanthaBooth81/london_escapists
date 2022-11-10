from django.contrib import admin
from .models import TravelDestinations


class TravelDestinationAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'destination_image',
        'destination',
        'created_on',
        'updated_on',
        'intro',
        'activities',
        'activity_image',
        'food',
        'food_image',
        'additional_info',
        'additional_image',
        'top_destination',
    )


admin.site.register(TravelDestinations, TravelDestinationAdmin)