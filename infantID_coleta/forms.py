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
        widgets = {
            'id_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'nome_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'telefone_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'endereco_cadastro':forms.TextInput(attrs={'class':'form-control'}),
            'bairro_cadastro':forms.TextInput(attrs={'class':'form-control'}),
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
        widgets = {
            'id_cadastro':forms.TextInput(attrs={'class':'form-control'}),
            'peso':forms.TextInput(attrs={'class':'form-control'}),
            'altura':forms.TextInput(attrs={'class':'form-control'}),
            'semanas_gestacao':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.Select(attrs={'class':'form-control'}),
            'scanner':forms.TextInput(attrs={'class':'form-control'}),
            'data_coleta':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'observacao':forms.Textarea(attrs={'class':'form-control'}),
            'nome_hospital':forms.Select(attrs={'class':'form-control'}),
            'nome_coletista':forms.Select(attrs={'class':'form-control'}),
            'id_responsavel':forms.Select(attrs={'class':'form-control'}),
        }
class cadastro_coletista(forms.ModelForm):
    class Meta:
        model = Coletista
        exclude = ['']
        labels = {
            'nome':'Nome'
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
        }

class cadastro_hospital(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['']
        labels = {
            'nome':'Nome'
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
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
        widgets = {
            'data_agenda':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'tipo_rc':forms.Select(attrs={'class':'form-control'}),
            'id_cadastro':forms.Select(attrs={'class':'form-control'}),
            'id_responsavel':forms.Select(attrs={'class':'form-control'}),
            'id_recoleta':forms.Select(attrs={'class':'form-control'}),
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
        widgets ={
            'scanner':forms.TextInput(attrs={'class':'form-control'}),
            'data_recoleta':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'idcadastro':forms.Select(attrs={'class':'form-control'})
        }