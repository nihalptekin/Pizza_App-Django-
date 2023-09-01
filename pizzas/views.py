from django.shortcuts import render
from .models import Pizza

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