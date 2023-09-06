from django.shortcuts import render

def addproduct(request):
    return render(request,
        'manager/add_product.html'
    )

def home(request):
    return render (request,
    'manager/home.html')