from django.urls import path
from . import views as exchViews

urlpatterns = [
    path('exchange/', exchViews.exchangePage, name='exchange'),
]