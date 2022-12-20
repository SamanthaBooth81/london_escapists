"""Travel destinations models"""
from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


class TravelDestinations(models.Model):
    """Blog posts for travel destination visited"""
    # destination_id = models.IntegerField(primary_key=True)
    destination_image = models.ImageField(null=True, blank=True)
    destination = models.CharField(max_length=50, null=False, blank=False)
    destination_subheading = models.CharField(
        max_length=150, null=False, blank=True)
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
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Orders posts by date created using descending order"""
        ordering = ['-created_on']
        """Removes extra 's' from Model name"""
        verbose_name_plural = 'Travel Destinations'

    def __str__(self):
        return self.destination
