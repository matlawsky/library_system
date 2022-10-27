
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.signup, name='login'),
    path('logout', views.signup, name='logout'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('mybooks', views.mybooks, name='mybooks'),
]
