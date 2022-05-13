from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import MassangPage
from django.conf.urls.static import static

urlpatterns = [
    path('massanger/<str:ToUser_name>', MassangPage, name='massang')
]

