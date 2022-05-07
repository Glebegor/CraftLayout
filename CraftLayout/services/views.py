from django.shortcuts import render
from .models import OrderModel

def HomePage(request):
    Order = OrderModel.objects.all()
    Title = 'Home Page'
    data = {
        'Title': Title,
        'Order': Order
    }
    return render(request, 'services/home.html', data)

def servicePage(request):
    Order = OrderModel.objects.all()
    data ={
        'Order': Order
    }
    return render(request, 'services/service.html', data)

def serviceOnepage(request, id):
    Order = OrderModel.objects.filter(pk=id)
    data ={
        'Order': Order
    }
    return render(request, 'services/servicePage.html', data)