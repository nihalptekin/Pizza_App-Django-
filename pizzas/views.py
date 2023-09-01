from django.shortcuts import render, redirect
from .models import Pizza, Order

# Create your views here.
def home(request):
    context={
    }
    return render(request, 'pizzas/home.html', context)

def pizzas(request):
    pizzas=Pizza.objects.all()
    context={
        'pizzas': pizzas
    }
    return render(request, 'pizzas/pizzas.html', context)

from .forms import OrderForm
def order(request):
    pizza=Pizza.objects.all()
    form=OrderForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            order=form.save()
            return redirect('home')

    
    context={
        'pizza': pizza,
        'form':form
    }
    return render(request, 'pizzas/order.html', context)