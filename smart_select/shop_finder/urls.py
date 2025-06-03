 
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("", views.shop_finder, name='shop_finder'),  # shop finder page
    
]  