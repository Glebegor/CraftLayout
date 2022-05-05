from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('orders/', views.OrderPage, name='orders'),
]
