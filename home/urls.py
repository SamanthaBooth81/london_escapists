"""Home urls"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('destinations/', include(
        'travel_destinations.urls'), name='destinations'),
]
