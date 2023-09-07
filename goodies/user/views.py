from django.shortcuts import render

def Base(request):
    return render(request,
    'user/base.html'
    )

def Home(request):
    return render(request,
    'user/home.html'
    )

def Cart(request):
    return render(request,
    'user/cart.html'
    )

def Checkout(request):
    return render(request,
    'user/home.html'
    )

def Store(request):
    return render(request,
    'user/store.html'
    )

