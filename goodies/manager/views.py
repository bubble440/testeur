from django.shortcuts import render

def addproduct(request):
    return request(request,
        'goodies/add_product.html'
    )
