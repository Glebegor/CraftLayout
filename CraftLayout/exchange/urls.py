from django.urls import path
from . import views as exchViews

urlpatterns = [
    path('exchange/', exchViews.exchangePage, name='exchange'),
    path('exchange/<int:id>', exchViews.OrderPage),
    path('createOrder/', exchViews.DoOrderPage, name='createOrder')
]