 
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("", views.prediction, name='prediction'),  # price prediction page
    path("laptop/", views.laptop, name='laptop'),   #laptop price prediction
    path("tablet", views.tablet, name='tablet'),    #tablet price prediction
  
]  