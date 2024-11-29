from django import forms
from infantID_coleta.models import *


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['id_responsavel'], 'Ex: LC, JC2')
        add_placeholder(self.fields['nome_responsavel'], 'Ex: Jõao das Graças')
        add_placeholder(self.fields['telefone_responsavel'], 'Ex: 46992143985')
        add_placeholder(self.fields['endereco_cadastro'], 'Ex: Av. Tupi')
        add_placeholder(self.fields['bairro_cadastro'], 'Ex: Centro')
        
class cadastro_coleta(forms.ModelForm):
    class Meta:
        model = Cadastro
        exclude = ['id_cadastro',]
        labels = {
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['peso'], 'Ex: 3.781')
        add_placeholder(self.fields['altura'], 'Em Cm, ex: 55')
        add_placeholder(self.fields['semanas_gestacao'], 'Ex: 32')
        add_placeholder(self.fields['semanas_gestacao'], 'Ex: Scanner1')


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

class cadastro_Recoleta(forms.ModelForm):
    class Meta:
        model = Recoleta
        exclude = ['id_recoleta']
        labels = {
            'scanner':'Scanner',
            'data_recoleta':'Data da Recoleta',
            'idcadastro':'ID Cadastrado',
        }