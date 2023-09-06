
from django.contrib import admin
from django.urls import path
from manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.addproduct),
    path('home/', views.home),
]
