from django import forms
from infantID_coleta.models import *
from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class cadastro_responsavel(forms.ModelForm):
    class Meta:
        model = Responsvel
        exclude = ['endereco_atual', 'bairro_atual', ]
        labels = {
            'pais': '',
            'id_responsavel':'ID',
            'nome_responsavel':'Nome do Responsável',
            'telefone_responsavel':'Telefone',
            'cep': 'CEP',
            'estado': 'Estado',
            'cidade': 'Cidade',
            'bairro_cadastro':'Bairro',
            'endereco_cadastro':'Endereço',
        }
        widgets = {
            'pais': forms.HiddenInput(),
            'id_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'nome_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'telefone_responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'cep':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'required': 'required'}),
            'endereco_cadastro':forms.TextInput(attrs={'class':'form-control'}),
            'bairro_cadastro':forms.TextInput(attrs={'class':'form-control'}),

        }

        def clean_cep(self):
            cep = self.cleaned_data['cep']
            return cep.replace('-', '')
        
        def clean(self):
            cleaned_data = super().clean()
            cidade = cleaned_data.get('cidade')
            estado = cleaned_data.get('estado')
            cep = cleaned_data.get('cep')
            if not cidade or not estado or (cep<8):
                raise forms.ValidationError("Preencha todos os campos.")


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
            'n_dedos':'Nº de Dedos Coletados',
            'justificativa':'Justificativa',
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
            'n_dedos':forms.TextInput(attrs={'class':'form-control'}),
            'justificativa':forms.Textarea(
                attrs={'class':'form-control', 'rows':'3'}
                ),
            'scanner':forms.TextInput(attrs={'class':'form-control'}),
            'data_coleta':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'observacao':forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'nome_hospital':forms.Select(attrs={'class':'form-control'}),
            'nome_coletista':forms.Select(attrs={'class':'form-control'}),
            'id_responsavel':forms.Select(attrs={'class':'form-control'}),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['peso'], 'Ex: 3.781')
        add_placeholder(self.fields['altura'], 'Em Cm, ex: 55')
        add_placeholder(self.fields['semanas_gestacao'], 'Ex: 32')
        add_placeholder(self.fields['scanner'], 'Ex: Scanner1')
        add_placeholder(self.fields['n_dedos'], 'Deve ser maior ou igual a 14')


    
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
            'n_dedos':'Nº de Dedos Coletados',
            'justificativa':'Justificativa',
        }
        widgets ={
            'scanner':forms.TextInput(attrs={'class':'form-control'}),
            'n_dedos':forms.TextInput(attrs={'class':'form-control'}),
            'justificativa':forms.Textarea(
                attrs={'class':'form-control', 'rows':'3'}
                ),
            'data_recoleta':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'idcadastro':forms.Select(attrs={'class':'form-control'})
        }


class alteracao_endereco(forms.ModelForm):
    responsavel = forms.ModelChoiceField(
        queryset=Responsvel.objects.all(),
        to_field_name="nome_responsavel",
        required=True,
        widget=forms.TextInput(attrs={'class': 'autocomplete form-control', 'id': 'id_responsavel'}), 
        label='Responsável')
    
    cep_atualizado = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_cep'}),  
        label='CEP')
    
    cidade_atualizado = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_cidade', 'readonly': True}),  
        label='Cidade')
    
    estado_atualizado = forms.CharField(
        max_length=2,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_estado', 'readonly': True}),  
        label='Estado')
    
    pais_atualizado = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.HiddenInput(attrs={'id': 'id_pais'}),
        label=''
    )
    
    class Meta:
        model = HistoricoEndereco
        fields = ("responsavel", "cep_atualizado", "cidade_atualizado", "estado_atualizado", "bairro_atualizado", "endereco_atualizado")

        labels = {
            'pais_atualizado': '',
            'responsavel':'Nome do Responsável',
            'cep_atualizado': 'CEP',
            'bairro_atualizado':'Bairro',
            'endereco_atualizado':'Endereço',
        }
        widgets = {
            'pais_atualizado': forms.HiddenInput(),
            'responsavel':forms.TextInput(attrs={'class':'form-control'}),
            'cep_atualizado':forms.TextInput(attrs={'class':'form-control'}),
            'endereco_atualizado':forms.TextInput(attrs={'class':'form-control'}),
            'bairro_atualizado':forms.TextInput(attrs={'class':'form-control'}),
        }

        def clean_cep_atualizado(self):
            cep_atualizado = self.cleaned_data['cep_atualizado']
            return cep_atualizado.replace('-', '')



class alteracao_telefone(forms.ModelForm):
    responsavel = forms.ModelChoiceField(
        queryset=Responsvel.objects.all(),
        to_field_name="nome_responsavel",
        required=True,
        widget=forms.TextInput(attrs={'class': 'autocomplete form-control', 'id': 'id_responsavel'}), 
        label='Responsável')

    class Meta:
        model = HistoricoTelefone
        fields = ('responsavel', 'telefone_atualizado')
        exclude = ['telefone_antigo']

        labels = {'telefone_atualizado': 'Telefone'}
        widgets = {'telefone_atualizado':forms.TextInput(attrs={'class':'form-control'})}

        def clean(self):
            cleaned_data = super().clean()
            responavel = cleaned_data.get('responsavel')
            telefone = cleaned_data.get('telefone_atualizado')
            if not responavel or not telefone:
                raise forms.ValidationError("Preencha todos os campos.")