# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    choices_rc = [
        ('7 Dias', '7 Dias'),
        ('14 Dias', '14 Dias'),
        ('1 Mês', '1 Mes'),
        ('2 Meses', '2 Meses'),
        ('3 Meses', '3 Meses'),
        ('6 Meses', '6 Meses'),
        ('1 Ano', '1 Ano'), 
    ]
    id_agenda = models.AutoField(primary_key=True, serialize=True)
    data_agenda = models.DateField(blank=True, null=True)
    tipo_rc = models.CharField(max_length=20,choices=choices_rc, blank=True, null=True)
    id_cadastro = models.ForeignKey('Cadastro', models.DO_NOTHING, db_column='id_cadastro', blank=True, null=True)
    id_responsavel = models.ForeignKey('Responsvel', models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)
    id_recoleta = models.ForeignKey('Recoleta', models.DO_NOTHING, db_column='id_recoleta', blank=True, null=True)

    class Meta:
        db_table = 'agenda'

    def __str__(self):
        return f'{self.tipo_rc} - {self.data_agenda} | {self.id_responsavel.nome_responsavel}'


class Cadastro(models.Model):
    opcoes_sexo = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    id_cadastro = models.CharField(primary_key=True, max_length=10)
    peso = models.FloatField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    semanas_gestacao = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1,choices=opcoes_sexo, blank=True, null=True)
    n_dedos = models.PositiveIntegerField(blank=True, null=True)
    justificativa = models.CharField(max_length=30, blank=True, null=True)
    scanner = models.CharField(max_length=20, blank=True, null=True)
    data_coleta = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    nome_hospital = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='nome_hospital', blank=True, null=True)
    nome_coletista = models.ForeignKey('Coletista', models.DO_NOTHING, db_column='nome_coletista', blank=True, null=True)
    id_responsavel = models.ForeignKey('Responsvel', models.DO_NOTHING, db_column='id_responsavel', blank=True, null=True)

    class Meta:
        db_table = 'cadastro'
        

    def __str__(self):
        return f'ID: {self.id_cadastro} - {self.id_responsavel.nome_responsavel}'


class Coletista(models.Model):
    nome = models.CharField(primary_key=True, max_length=45)

    class Meta:
        db_table = 'coletista'

    def __str__(self):
        return self.nome


class Desvinculo(models.Model):
    id_desvinculo = models.AutoField(serialize=True, primary_key=True)
    data_desvinculo = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=50, blank=True, null=True)
    id_cadastro = models.ForeignKey(Cadastro, models.DO_NOTHING, db_column='id_cadastro', blank=True, null=True)
    idresponsavel = models.ForeignKey('Responsvel', models.DO_NOTHING, db_column='idresponsável', blank=True, null=True)

    class Meta:
        db_table = 'desvinculo'

    def __str__(self):
        return f'{self.idresponsavel.nome_responsavel} - {self.data_desvinculo}'



class Hospital(models.Model):
    nome = models.CharField(primary_key=True, max_length=45)

    class Meta:
        db_table = 'hospital'
    
    def __str__(self):
        return self.nome


class Materiais(models.Model):
    id_materiais = models.AutoField(primary_key=True)
    carteirinha = models.BooleanField(blank=True, null=True)
    mordedor = models.BooleanField(blank=True, null=True)
    gorro = models.BooleanField(blank=True, null=True)
    id_cadastro = models.ForeignKey(Cadastro, models.DO_NOTHING, db_column='id_cadastro', blank=True, null=True)

    class Meta:
        db_table = 'materiais'



class Recoleta(models.Model):
    id_recoleta = models.AutoField(serialize=True, primary_key=True)
    scanner = models.CharField(max_length=20, blank=True, null=True)
    n_dedos = models.PositiveIntegerField(blank=True, null=True)
    justificativa = models.CharField(max_length=30, blank=True, null=True)
    data_recoleta = models.DateField(blank=True, null=True)
    idcadastro = models.ForeignKey(Cadastro, models.DO_NOTHING, db_column='idcadastro', blank=True, null=True)

    class Meta:
        db_table = 'recoleta'

    def __str__(self):
        return f'{self.idcadastro} - {self.data_recoleta}'


class Responsvel(models.Model):
    id_responsavel = models.CharField(primary_key=True, max_length=10)
    nome_responsavel = models.CharField(max_length=45, blank=True, null=True)
    telefone_responsavel = models.CharField(max_length=11, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)  
    estado = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=50, blank=False, null=False)
    bairro_cadastro = models.CharField(max_length=20, blank=True, null=True)
    endereco_cadastro = models.CharField(max_length=45, blank=True, null=True)
    endereco_atual = models.CharField(max_length=45, blank=True, null=True)
    bairro_atual = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)  # Captura a data de criação

    class Meta:
        db_table = 'responsavel'

    def __str__(self):
        return f'{self.id_responsavel} - {self.nome_responsavel}'
    

class HistoricoEndereco(models.Model):
    responsavel = models.ForeignKey('Responsvel', models.DO_NOTHING, db_column='responsavel', blank=True, null=True)
    cep_atualizado = models.CharField(max_length=10, blank=True, null=True)  
    estado_atualizado = models.CharField(max_length=50, blank=True, null=True)
    cidade_atualizado = models.CharField(max_length=50, blank=True, null=True)
    bairro_atualizado = models.CharField(max_length=20, blank=True, null=True)
    endereco_atualizado = models.CharField(max_length=45, blank=True, null=True)
    pais_atualizado = models.CharField(max_length=50, blank=True, null=True)
    cep_antigo = models.CharField(max_length=10, blank=True, null=True)  
    estado_antigo = models.CharField(max_length=50, blank=True, null=True)
    cidade_antigo = models.CharField(max_length=50, blank=True, null=True)
    bairro_antigo = models.CharField(max_length=20, blank=True, null=True)
    endereco_antigo = models.CharField(max_length=45, blank=True, null=True)
    pais_antigo = models.CharField(max_length=50, blank=True, null=True)
    data_alteracao = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'historico_endereco'


class HistoricoTelefone(models.Model):
    responsavel = models.ForeignKey('Responsvel', models.DO_NOTHING, db_column='responsavel', blank=False, null=True)
    telefone_antigo = models.CharField(max_length=11, blank=False, null=True)
    telefone_atualizado = models.CharField(max_length=11, blank=False, null=True)

    class Meta:
        db_table = 'historico_telefone'
