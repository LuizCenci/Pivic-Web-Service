# Generated by Django 5.1.3 on 2025-02-26 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coletista',
            fields=[
                ('nome', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'coletista',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('nome', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Responsvel',
            fields=[
                ('id_responsavel', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome_responsavel', models.CharField(blank=True, max_length=45, null=True)),
                ('telefone_responsavel', models.CharField(blank=True, max_length=11, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro_cadastro', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco_cadastro', models.CharField(blank=True, max_length=45, null=True)),
                ('endereco_atual', models.CharField(blank=True, max_length=45, null=True)),
                ('bairro_atual', models.CharField(blank=True, max_length=20, null=True)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'responsavel',
            },
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id_cadastro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('altura', models.IntegerField(blank=True, null=True)),
                ('semanas_gestacao', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
                ('n_dedos', models.PositiveIntegerField(blank=True, null=True)),
                ('justificativa', models.CharField(blank=True, max_length=30, null=True)),
                ('scanner', models.CharField(blank=True, max_length=20, null=True)),
                ('data_coleta', models.DateField(blank=True, null=True)),
                ('observacao', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_coletista', models.ForeignKey(blank=True, db_column='nome_coletista', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.coletista')),
                ('nome_hospital', models.ForeignKey(blank=True, db_column='nome_hospital', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.hospital')),
                ('id_responsavel', models.ForeignKey(blank=True, db_column='id_responsavel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.responsvel')),
            ],
            options={
                'db_table': 'cadastro',
            },
        ),
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id_materiais', models.AutoField(primary_key=True, serialize=False)),
                ('carteirinha', models.BooleanField(blank=True, null=True)),
                ('mordedor', models.BooleanField(blank=True, null=True)),
                ('gorro', models.BooleanField(blank=True, null=True)),
                ('id_cadastro', models.ForeignKey(blank=True, db_column='id_cadastro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.cadastro')),
            ],
            options={
                'db_table': 'materiais',
            },
        ),
        migrations.CreateModel(
            name='Recoleta',
            fields=[
                ('id_recoleta', models.AutoField(primary_key=True, serialize=False)),
                ('scanner', models.CharField(blank=True, max_length=20, null=True)),
                ('n_dedos', models.PositiveIntegerField(blank=True, null=True)),
                ('justificativa', models.CharField(blank=True, max_length=30, null=True)),
                ('data_recoleta', models.DateField(blank=True, null=True)),
                ('idcadastro', models.ForeignKey(blank=True, db_column='idcadastro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.cadastro')),
            ],
            options={
                'db_table': 'recoleta',
            },
        ),
        migrations.CreateModel(
            name='HistoricoEndereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep_atualizado', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_atualizado', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade_atualizado', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro_atualizado', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco_atualizado', models.CharField(blank=True, max_length=45, null=True)),
                ('pais_atualizado', models.CharField(blank=True, max_length=50, null=True)),
                ('cep_antigo', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_antigo', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade_antigo', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro_antigo', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco_antigo', models.CharField(blank=True, max_length=45, null=True)),
                ('pais_antigo', models.CharField(blank=True, max_length=50, null=True)),
                ('data_alteracao', models.DateField(auto_now_add=True)),
                ('responsavel', models.ForeignKey(blank=True, db_column='responsavel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.responsvel')),
            ],
            options={
                'db_table': 'historico_endereco',
            },
        ),
        migrations.CreateModel(
            name='Desvinculo',
            fields=[
                ('id_desvinculo', models.AutoField(primary_key=True, serialize=False)),
                ('data_desvinculo', models.DateField(blank=True, null=True)),
                ('motivo', models.CharField(blank=True, max_length=50, null=True)),
                ('id_cadastro', models.ForeignKey(blank=True, db_column='id_cadastro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.cadastro')),
                ('idresponsavel', models.ForeignKey(blank=True, db_column='idresponsável', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.responsvel')),
            ],
            options={
                'db_table': 'desvinculo',
            },
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id_agenda', models.AutoField(primary_key=True, serialize=False)),
                ('data_agenda', models.DateField(blank=True, null=True)),
                ('tipo_rc', models.CharField(blank=True, choices=[('7 Dias', '7 Dias'), ('14 Dias', '14 Dias'), ('1 Mês', '1 Mes'), ('2 Meses', '2 Meses'), ('3 Meses', '3 Meses'), ('6 Meses', '6 Meses'), ('1 Ano', '1 Ano')], max_length=20, null=True)),
                ('id_cadastro', models.ForeignKey(blank=True, db_column='id_cadastro', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.cadastro')),
                ('id_recoleta', models.ForeignKey(blank=True, db_column='id_recoleta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.recoleta')),
                ('id_responsavel', models.ForeignKey(blank=True, db_column='id_responsavel', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='infantID_coleta.responsvel')),
            ],
            options={
                'db_table': 'agenda',
            },
        ),
    ]
