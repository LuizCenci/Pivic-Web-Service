from django import forms
from infantID_coleta.models import *

class cadastro_responsavel(forms.ModelForm):
    class Meta:
        model = Responsvel
        exclude = ['endereco_atual', 'bairro_atual']
        labels = {
            'id_responsavel':'ID',
            'nome_responsavel':'Nome do Responsável',
            'telefone_responsavel':'Telefone',
            'endereco_cadastro':'Endereço',
            'bairro_cadastro':'Bairro',
        }
        
class cadastro_coleta(forms.ModelForm):
    class Meta:
        model = Cadastro
        exclude = ['',]
        labels = {
            'id_cadastro':'ID',
            'peso':'Peso',
            'altura':'Altura',
            'semanas_gestacao':'Semanas de Gestação',
            'sexo':'Sexo',
            'scanner':'Scanner',
            'data_coleta':'Data da Coleta',
            'observacao':'Observações',
            'nome_hospital':'Selecionar Hospital',
            'nome_coletista':'Selecionar Coletista',
            'id_responsavel':'Selecionar Responsável'
        }

class cadastro_coletista(forms.ModelForm):
    class Meta:
        model = Coletista
        exclude = ['']
        labels = {
            'nome':'Nome'
        }

class cadastro_hospital(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['']
        labels = {
            'nome':'Nome'
        }

class cadastro_Agenda(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ['id_agenda']
        labels = {
            'data_agenda':'Data da Recoleta',
            'tipo_rc':'Tipo de Recoleta',
            'id_cadastro':'Selecionar Cadastro',
            'id_responsavel':'Selecionar Responsável',
            'id_recoleta':'Selecionar Recoleta',
        }