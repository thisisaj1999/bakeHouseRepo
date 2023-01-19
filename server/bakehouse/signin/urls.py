from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('form', views.form, name='form'),
]
