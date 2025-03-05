from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import Http404
from infantID_coleta.models import *
from infantID_coleta.forms import *
from django.contrib import messages


def index(request):
    cadastros = Cadastro.objects.order_by('-data_coleta')[:5]
    agenda = Agenda.objects.order_by('-data_agenda')[:5]
    context = {'cadastros':cadastros, 'agenda':agenda}
    return render(request, 'pages/index.html', context)


def novo_responsavel(request):
    if request.method == 'POST':
        form = cadastro_responsavel(request.POST)
        if form.is_valid():
            responsavel = form.save(commit=False)
            responsavel.endereco_atual = responsavel.endereco_cadastro
            responsavel.bairro_atual = responsavel.bairro_cadastro
            responsavel.save()
            messages.success(request, 'Responsável adicionado com sucesso!')
            return redirect('formulario:index')
        else:
            messages.error(request, 'Preencha todos os campos.')
            responsavel = cadastro_responsavel()
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



def nova_recoleta_view(request):
    recoleta_form_data = request.session.get('recoleta_form_data', None)
    form = cadastro_Recoleta(recoleta_form_data)
    context = {'form':form}
    return render(request, 'pages/nova_recoleta.html', context)



def nova_recoleta_create(request):
    if not request.POST:
        raise Http404
    
    POST = request.POST
    request.session['recoleta_form_data'] = POST

    form = cadastro_Recoleta(POST)
    if form.is_valid():
        infos = form.save(commit=False)

        n_dedos = infos.n_dedos
        if n_dedos < 14 and not infos.justificativa:
            messages.error(request, 'Como o número de dedos foi menor que 14, deve fornecer uma justificativa')
            return redirect('formulario:nova_recoleta')
        
        infos.save()

        del request.session['recoleta_form_data']

        messages.success(request, 'Recoleta adicionada com sucesso!')

        return redirect('formulario:index')

    return redirect('formulario:nova_recoleta')



def alterar_endereco(request):
    if request.method == 'POST':
        form = alteracao_endereco(request.POST)
        if form.is_valid():
            responsavel = form.cleaned_data['responsavel']
            form.instance.cep_antigo = responsavel.cep
            form.instance.cidade_antigo = responsavel.cidade
            form.instance.estado_antigo = responsavel.estado
            form.instance.bairro_antigo = responsavel.bairro_atual
            form.instance.endereco_antigo = responsavel.endereco_atual
            form.instance.pais_antigo = responsavel.pais
            form.instance.pais_atualizado = form.cleaned_data['pais_atualizado']
            responsavel.cep = form.cleaned_data['cep_atualizado']
            responsavel.endereco_atual = form.cleaned_data['endereco_atualizado']
            responsavel.bairro_atual = form.cleaned_data['bairro_atualizado']
            form.save()
            responsavel.save()
            messages.success(request, 'Endereço alterado com sucesso!')

        return redirect('formulario:index')
    else:

        form = alteracao_endereco()

    context = {'form': form}
    return render(request, 'pages/alterar_endereco.html', context)



def alterar_telefone(request):
    if request.method == "POST":
        form = alteracao_telefone(request.POST)
        print(form)
        if form.is_valid:
            responsavel = form.cleaned_data['responsavel']
            form.instance.telefone_antigo = responsavel.telefone_responsavel
            responsavel.telefone_responsavel = form.cleaned_data['telefone_atualizado']
            form.save()
            responsavel.save()
            messages.success(request, 'Telefone alterado com sucesso!')
            return redirect('formulario:index')
        else:
            messages.error(request, 'Preencha todos os dados corretamente.')
            form = alteracao_telefone()
        
    else:
        form = alteracao_telefone()


    context ={'form': form}
    return render(request, 'pages/alterar_telefone.html', context)

def buscar_responsavel(request):
    if 'q' in request.GET:
        query = request.GET['q']
        responsaveis = Responsvel.objects.filter(nome_responsavel__icontains=query)  # Busca no nome_responsavel
        results = [{'nome_responsavel': r.nome_responsavel, 'id_responsavel': r.id_responsavel} for r in responsaveis]  # Retorna nome e id
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})

def atualizacao_cadastral(request):
    return render(request, 'pages/atualizacao_cadastral.html')

