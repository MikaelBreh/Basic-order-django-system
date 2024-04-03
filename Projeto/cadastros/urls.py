from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientesList.as_view(), name='home'),
    path('cadastro_cliente', views.ClienteCreate.as_view(), name='cadastro_cliente'),

]