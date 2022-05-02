from django.shortcuts import render
from .models import Exchange

def exchangePage(request):
    orders = Exchange.objects.all()
    context = {'data': orders}
    return render(request, 'exchange/exchange.html', context)

def OrderPage(request, id):
    orders = Exchange.objects.filter(pk=id)
    context = {'data': orders}
    return render(request, 'exchange/exchangeOrder.html', context)
