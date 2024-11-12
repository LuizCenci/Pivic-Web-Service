from django.contrib import admin
from infantID_coleta.models import *
from django.apps import apps


admin.site.register(Agenda)
admin.site.register(Cadastro)
admin.site.register(Coletista)
admin.site.register(Desvinculo)
admin.site.register(Hospital)
admin.site.register(Materiais)
admin.site.register(Recoleta)
admin.site.register(Responsvel)