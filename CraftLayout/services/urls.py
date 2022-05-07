from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('service/', views.servicePage, name='service'),
    path('service/<int:id>', views.serviceOnepage, name='serviceOne'),
]
