from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brand', views.brand, name='brand'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
