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
        