from django.shortcuts import render
from .models import OrderModel

def HomePage(request):
    Title = 'Home Page'
    return render(request, 'services/home.html', {'Title':Title})

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