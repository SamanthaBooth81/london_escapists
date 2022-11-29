"""Travel Destinations App URLs"""
from django.urls import path
from . import views


urlpatterns = [
    path("all-destinations/", views.all_destinations,
         name="destinations"),
    path("add-destinations/", views.add_destinations,
         name="add_destinations"),
]
