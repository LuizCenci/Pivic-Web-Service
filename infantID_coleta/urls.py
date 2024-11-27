from django.urls import path, include
from infantID_coleta.views import *

app_name = 'formulario'
urlpatterns = [
    path('', index, name='index'),
    path('novo-responsavel/', novo_responsavel, name='novo_responsavel'),
    path('novo-cadastro/', novo_cadastro, name='novo_cadastro'),
    path('novo-coletista/', novo_coletista, name='novo_coletista'),
    path('novo-hospital/', novo_hospital, name='novo_hospital'),
    path('nova-agenda/', nova_agenda, name='nova_agenda'),
    path('nova-recoleta/', nova_recoleta, name='nova_recoleta'),
]       
