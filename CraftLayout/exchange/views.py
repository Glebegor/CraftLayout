from django.shortcuts import render, redirect
from .models import Exchange
from .forms import FormExchange
def exchangePage(request):
    orders = Exchange.objects.all()
    context = {'data': orders}
    return render(request, 'exchange/exchange.html', context)

def OrderPage(request, id):
    orders = Exchange.objects.filter(pk=id)
    context = {'data': orders}
    return render(request, 'exchange/exchangeOrder.html', context)

def DoOrderPage(request):
    if request.method == "POST":
        form = FormExchange(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            return redirect('/exchange/' + str(order.id) )
    else:
        form = FormExchange()
    return render(request, 'exchange/createExchange.html', {'form': form})