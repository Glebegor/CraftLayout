from django.shortcuts import render
from .models import OrderModel

def HomePage(request):
    Title = 'Home Page'
    return render(request, 'services/home.html', {'Title':Title})

def OrderPage(request):
    Order = OrderModel.objects.all()
    data ={
        'Order': Order
    }
    return render(request, 'services/orders.html', data)
