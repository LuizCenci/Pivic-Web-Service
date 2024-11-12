from django.shortcuts import render, redirect
from infantID_coleta.models import *
from infantID_coleta.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def novo_responsavel(request):
    responsavel = cadastro_responsavel()
    if request.method == 'POST':
        responsavel = cadastro_responsavel(request.POST)
        if responsavel.is_valid():
            responsavel.save()
            return redirect('formulario:index')

    context = {'form':responsavel}
    return render(request, 'novo_responsavel.html', context)

def novo_cadastro(request):
    cadastro = cadastro_coleta()
    if request.method == 'POST':
        cadastro = cadastro_coleta(request.POST)
        if cadastro.is_valid():
            cadastro.save()
            return redirect('formulario:index')

    context = {'form':cadastro}
    return render(request, 'novo_cadastro.html', context)

def novo_coletista(request):
    coletista = cadastro_coletista()
    if request.method == 'POST':
        coletista = cadastro_coletista(request.POST)
        if coletista.is_valid():
            coletista.save()
            return redirect('formulario:index')

    context = {'form':coletista}
    return render(request, 'novo_coletista.html', context)

def novo_hospital(request):
    hospital = cadastro_hospital()
    if request.method == 'POST':
        hospital = cadastro_hospital(request.POST)
        if hospital.is_valid():
            hospital.save()
            return redirect('formulario:index')

    context = {'form':hospital}
    return render(request, 'novo_hospital.html', context)

def nova_agenda(request):
    agenda = cadastro_Agenda()
    if request.method == 'POST':
        agenda = cadastro_Agenda(request.POST)
        if agenda.is_valid():
            agenda.save()
            return redirect('formulario:index')

    context = {'form':agenda}
    return render(request, 'nova_agenda.html', context)