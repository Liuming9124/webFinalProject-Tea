from django.shortcuts import render
from .models import Order, Drink
from .forms import OrderForm
from django.http import HttpResponse

def elements(request):
    
    return render(
        request,
        'bonus/elements.html',
    )

def generic(request):

    return render(
        request,
        'bonus/generic.html',
    )


def success(request):

    return render(
        request,
        'bonus/success.html',
    )

def index(request):
    drinklist = Drink.objects.all()

    if request.method == "POST":
        form = OrderForm(request.POST)
        form.save()
        return render(request, "bonus/success.html", context = {'drink_list': drinklist, 'form': form})
    form = OrderForm()
    
    
    return render(
        request,
        "bonus/index.html",
        context = {'drink_list': drinklist, 'form':form }
        )
