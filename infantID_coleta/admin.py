from django.contrib import admin
from infantID_coleta.models import *
from django.apps import apps


# Obtenha todos os models da aplicação
models = apps.get_models()

# Registre cada model automaticamente
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        # Ignora se o model já está registrado
        pass
