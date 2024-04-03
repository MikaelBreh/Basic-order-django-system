from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-pedidos'),
    path('obter-informacoes-cliente/', views.obter_informacoes_cliente, name='obter_informacoes_cliente'),

]