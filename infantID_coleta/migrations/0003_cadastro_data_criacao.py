# Generated by Django 5.1.3 on 2025-03-03 13:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infantID_coleta', '0002_responsvel_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
