"""Travel destinations models"""
from django.db import models


class TravelDestinations(models.Model):
    """Blog posts for travel destination visited"""
    destination_image = models.ImageField(null=True, blank=True)
    destination = models.CharField(max_length=50, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    intro = models.TextField(max_length=500, blank=True)
    activities = models.TextField(max_length=500, blank=True)
    activity_image = models.ImageField(null=True, blank=True)
    food = models.TextField(max_length=500, blank=True)
    food_image = models.ImageField(null=True, blank=True)
    additional_info = models.TextField(max_length=500, blank=True)
    additional_image = models.ImageField(null=True, blank=True)
    top_destination = models.BooleanField(default=False)
