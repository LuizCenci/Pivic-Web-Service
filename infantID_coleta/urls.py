from django.urls import path, include
from infantID_coleta.views import *

app_name = 'formulario'
urlpatterns = [
    path('', index, name='index'),
    path('novo-responsavel/', novo_responsavel, name='novo_responsavel'),
    path('novo-cadastro/', novo_cadastro_view, name='novo_cadastro'),
    path('novo-cadastro/create', novo_cadastro_create, name='novo_cadastro_create'),
    path('novo-coletista/', novo_coletista, name='novo_coletista'),
    path('novo-hospital/', novo_hospital, name='novo_hospital'),
    path('nova-agenda/', nova_agenda, name='nova_agenda'),
    path('nova-recoleta/', nova_recoleta_view, name='nova_recoleta'),
    path('nova-recoleta/create', nova_recoleta_create, name='nova_recoleta_create'),
    path('alterar-endereco', alterar_endereco, name='alterar_endereco'),
    path('buscar-responsavel/', buscar_responsavel, name='buscar_responsavel'),
]       
