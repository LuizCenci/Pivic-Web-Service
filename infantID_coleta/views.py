from django.shortcuts import render, redirect
from infantID_coleta.models import *
from infantID_coleta.forms import *

# Create your views here.
def novo_responsavel(request):
    responsavel = cadastro_responsavel(request.POST)
    if request.method == 'POST':
        if responsavel.is_valid():
            responsavel.save()

    context = {'form':responsavel}
    return render(request, 'index.html', context)