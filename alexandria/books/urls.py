from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addbook', views.addbook, name='addbook'),
    path('deletebook', views.deletebook, name='deletebook'),
    path('returnbook', views.returnbook, name='returnbook'),
    path('borrowbook', views.borrowbook, name='borrowbook'),
    path('requestbook', views.requestbook, name='requestbook'),
    path('reservebook', views.reservebook, name='reservebook'),
]
