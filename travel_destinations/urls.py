"""Travel Destinations App URLs"""
from django.urls import path
from . import views


urlpatterns = [
    path("all-destinations/", views.ViewAllDestinations.as_view(),
         name="destinations"),
]
