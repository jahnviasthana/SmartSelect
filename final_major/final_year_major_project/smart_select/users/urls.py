 
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("", views.landing, name='landing'),   #landing page
    path("login/", views.login, name='login'),    #login
    path("signup/", views.signup, name='signup'),     #sign up
    path("about/", views.about, name='about'),     # about 
    path("forget_password/", views.forget_password, name='forget_password'),     # forget page
]  