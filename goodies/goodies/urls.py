
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home, name = "home"),
    path('cart/', views.Cart, name = "cart"),
    path('checkout/', views.Checkout, name = "checkout"),
    path('store/', views.Store, name = "store"),
]
