from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("userpage", views.userpage, name='userpage'),
    path("register", views.register, name='register')
]