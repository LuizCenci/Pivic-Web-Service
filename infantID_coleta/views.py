from django.shortcuts import render, redirect
from django.http import Http404
from infantID_coleta.models import *
from infantID_coleta.forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def novo_responsavel(request):
    if request.method == 'POST':
        responsavel = cadastro_responsavel(request.POST)
        if responsavel.is_valid():
            responsavel.save()
            messages.success(request, 'Responsável adicionado com sucesso!')
            return redirect('formulario:index')
    else:
        responsavel = cadastro_responsavel()

    context = {'form':responsavel}
    return render(request, 'pages/novo_responsavel.html', context)


def novo_cadastro_view(request):
    cadastro_form_data = request.session.get('cadastro_form_data', None)
    form = cadastro_coleta(cadastro_form_data)
    context = {'form': form}
    return render(request, 'pages/novo_cadastro.html', context)



def novo_cadastro_create(request):
    if not request.POST:
        raise Http404
    
    POST = request.POST
    request.session['cadastro_form_data'] = POST

    form = cadastro_coleta(POST)
    if form.is_valid():
        infos = form.save(commit=False)
        
        n_dedos = infos.n_dedos
        if n_dedos < 14 and not infos.justificativa:
            messages.error(request, 'Como o número de dedos foi menor que 14, deve fornecer uma justificativa')
            return redirect('formulario:novo_cadastro')
        
        n_filhos = Cadastro.objects.filter(id_responsavel=infos.id_responsavel).count()
        infos.id_cadastro = f'{infos.id_responsavel.id_responsavel}_0{n_filhos + 1}'
        infos.save()
        del request.session['cadastro_form_data']

        messages.success(request, 'Cadastro criado com sucesso!')

        return redirect('formulario:index') 
    return redirect('formulario:novo_cadastro')    




def novo_coletista(request):
    coletista = cadastro_coletista()
    if request.method == 'POST':
        coletista = cadastro_coletista(request.POST)
        if coletista.is_valid():
            coletista.save()
            messages.success(request, 'Coletista adicionado com sucesso!')
            return redirect('formulario:index')

    context = {'form':coletista}
    return render(request, 'pages/novo_coletista.html', context)


def novo_hospital(request):
    hospital = cadastro_hospital()
    if request.method == 'POST':
        hospital = cadastro_hospital(request.POST)
        if hospital.is_valid():
            hospital.save()
            messages.success(request, 'Hospital adicionado com sucesso!')
            return redirect('formulario:index')

    context = {'form':hospital}
    return render(request, 'pages/novo_hospital.html', context)


def nova_agenda(request):
    agenda = cadastro_Agenda()
    if request.method == 'POST':
        agenda = cadastro_Agenda(request.POST)
        if agenda.is_valid():
            agenda.save()
            messages.success(request, 'Agenda adicionada com sucesso!')
            return redirect('formulario:index')

    context = {'form':agenda}
    return render(request, 'pages/nova_agenda.html', context)

def nova_recoleta(request):
    recoleta = cadastro_Recoleta()
    if request.method == 'POST':
        recoleta = cadastro_Recoleta(request.POST)
        if recoleta.is_valid():
            recoleta.save()
            messages.success(request, 'Recoleta adicionada com sucesso!')
            return redirect('formulario:index')

    context = {'form':recoleta}
    return render(request, 'pages/nova_recoleta.html', context)
