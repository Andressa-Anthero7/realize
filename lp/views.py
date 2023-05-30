from django.shortcuts import render, redirect
from .models import Leads, Agendamento, Atendimento, Clientes, Perfil, Tagmeta, TagGoogle
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time


# Create your views here.


def index(request):
    if request.method == 'POST':
        nome_leads = request.POST.get('nome')
        email_leads = request.POST.get('email')
        whatsapp_leads = request.POST.get('whatsapp')
        status_aberto = 'fa-envelope'
        status_leads = 'NEUTRO'
        data_recebimento = datetime.now()
        Leads.objects.create(nome_leads=nome_leads,
                             email=email_leads,
                             whatsapp=whatsapp_leads,
                             status_aberto=status_aberto,
                             status_leads=status_leads,
                             data_recebimento=data_recebimento)
        leads = Leads.objects.last()

        return render(request, 'site/index.html')
    else:
        tag_meta = Tagmeta.objects.all()

        return render(request, 'site/index.html', {'tag_meta': tag_meta})


def abrirleads(request, pk):
    status_aberto = 'fa-envelope-open'
    Leads.objects.filter(pk=pk).update(status_aberto=status_aberto)


@login_required
def dashboard(request):
    leads = Leads.objects.all().order_by('-data_recebimento')
    return render(request, 'site/dashboard-v3.html', {'leads': leads})


@login_required
def atendimento(request, pk):
    leads_atendimento = Leads.objects.filter(pk=pk)
    atendimento_vinculado = Clientes.objects.filter(atendimento_vinculados_cliente=pk)

    agendamentos = Agendamento.objects.all()
    anotacoes = Atendimento.objects.filter(leads_atendimento=pk).order_by('-data_inclusao_atendimento')
    return render(request, 'site/atendimento.html', {'agendamentos': agendamentos,
                                                     'leads_atendimento': leads_atendimento,
                                                     'anotacoes': anotacoes,
                                                     'atendimento_vinculado': atendimento_vinculado})


def qualificar_leads(request, pk):
    if request.method == 'POST':
        status_leads = request.POST.get('opcionais-leads')
        print(status_leads)
        Leads.objects.filter(pk=pk).update(status_leads=status_leads)
        return redirect('atendimento', pk=pk)


def criar_agendamento(request):
    if request.method == 'POST':
        nome_agendamento = request.POST.get('nome_agendamento')
        data_evento = request.POST.get('data_evento')
        data_termino = request.POST.get('data_termino')
        data_agendamento = datetime.now()
        user_agendamento = request.user
        atendimento_vinculado = request.POST.get('atendimento-vinculado')
        Agendamento.objects.create(
            nome_agendamento=nome_agendamento,
            data_evento=data_evento,
            data_termino=data_termino,
            data_agendamento=data_agendamento,
            user_agendamento=user_agendamento,
            vinculado_ao_atendimento=atendimento_vinculado
        )

        return redirect('atendimento', pk=atendimento_vinculado)
    else:
        atendimento_vinculado = request.GET.get('atendimento-vinculado')
        return redirect('atendimento', pk=atendimento_vinculado)


def criar_atendimento(request):
    if request.method == 'POST':
        print('anotacoes_atendimento')
        anotacoes_atendimento = request.POST.get('anotacoes')

        atendimento_vinculado = request.POST.get('id_atendimento')
        data_inclusao_atendimento = datetime.now()
        user_logado_inclusao = request.user

        Atendimento.objects.create(
            anotacoes_atendimento=anotacoes_atendimento,
            leads_atendimento=atendimento_vinculado,
            data_inclusao_atendimento=data_inclusao_atendimento,
            user_inclusao_atendimento=user_logado_inclusao,

        )

        return redirect('atendimento', pk=atendimento_vinculado)
    else:
        atendimento_vinculado = request.GET.get('id_atendimento')
        return redirect('atendimento', pk=atendimento_vinculado)


def cadastrar_clientes(request):
    if request.method == 'POST':
        atendimento_vinculado = request.POST.get('atendimento_vinculado')
        nome_cliente = request.POST.get('nome_cliente')
        print(nome_cliente)
        email_cliente = request.POST.get('email_cliente')
        whatsapp_cliente = request.POST.get('whatsapp_cliente')

        Clientes.objects.create(
            atendimento_vinculados_cliente=atendimento_vinculado,
            nome_cliente=nome_cliente,
            email_cliente=email_cliente,
            whatsapp_cliente=whatsapp_cliente,

        )


def cadastro_cliente(request, pk):
    cliente = Clientes.objects.filter(atendimento_vinculados_cliente=pk)
    return render(request, 'site/cadastro_cliente.html', {'cliente': cliente})


def excluir_leads(request, pk):
    if request.method == 'POST':
        leads_excluir = Leads.objects.filter(pk=pk)
        leads_excluir.delete()
        return redirect('dashboard')
    else:
        return redirect('index')


def editar_agendamento(request, pk):
    if request.method == 'POST':
        nome_agendamento = request.POST.get('nome_agendamento')
        data_evento = request.POST.get('data_evento')
        data_termino = request.POST.get('data_termino')
        print(data_termino)
        data_agendamento = datetime.now()
        user = request.user
        user_agendamento = user.username
        print(user_agendamento)
        Agendamento.objects.filter(pk=pk).update(
            nome_agendamento=nome_agendamento,
            data_evento=data_evento,
            data_termino=data_termino,
            data_agendamento=data_agendamento,
            user_agendamento=user_agendamento,
        )

        return redirect('atendimento', pk=pk)
    else:
        return redirect('atendimento', pk=pk)


def deletar_agendamento(request, pk):
    if request.method == 'POST':
        agendamento_excluir = Agendamento.objects.filter(pk=pk)
        agendamento_excluir.delete()
        return redirect('atendimento', pk=pk)
    else:
        return redirect('atendimento', pk=pk)


@login_required
def configuracao(request, user):
    meta_tag = Tagmeta.objects.all()
    tag_google = TagGoogle.objects.all()
    logado = request.user.username
    if user == logado:
        perfil = Perfil.objects.filter(user_vinculado=user)
        print(perfil)
        return render(request, 'site/configuracao.html', {'perfil': perfil,
                                                          'user': user,
                                                          'meta_tag': meta_tag,
                                                          'tag_google': tag_google})
    else:
        return redirect(reverse('configuracao', args=[request.user]))


def add_img_perfil(request):
    if request.method == 'POST':
        img_perfil = request.FILES.get('img_perfil_add')
        user_vinculado = request.POST.get('user_vinculado')
        Perfil.objects.create(img_perfil=img_perfil,
                              user_vinculado=user_vinculado)
        return redirect(reverse('configuracao', args=[request.user]))


def editar_img_perfil(request):
    if request.method == 'POST':
        img_perfil = request.FILES.get('img_perfil_editar')
        user_vinculado = request.POST.get('user_vinculado_editar')
        Perfil.objects.get(user_vinculado=user_vinculado).delete()
        Perfil.objects.create(img_perfil=img_perfil,
                              user_vinculado=user_vinculado)
        return redirect(reverse('configuracao', args=[request.user]))


def add_meta_tag(request):
    if request.method == 'POST':
        editado_por = request.user.username
        data_atualizacao = datetime.now()
        tag_meta = request.POST.get('textarea-tag-pixel')
        tagmeta = Tagmeta.objects.all()
        for tagmeta in tagmeta:
            tagmeta.delete()
        Tagmeta.objects.create(editado_por=editado_por,
                               data_atualizacao=data_atualizacao,
                               tag_meta=tag_meta)
        return redirect(reverse('configuracao', args=[request.user]))
    else:
        return redirect(reverse('configuracao', args=[request.user]))


def add_tag_google(request):
    if request.method == 'POST':
        editado_por = request.user.username
        data_atualizacao = datetime.now()
        tag_google = request.POST.get('textarea-tag-google')
        tag_google_analitycs = TagGoogle.objects.all()
        for tag_google_analitycs in tag_google_analitycs:
            tag_google_analitycs.delete()
        TagGoogle.objects.create(editado_por=editado_por,
                                 data_atualizacao=data_atualizacao,
                                 tag_google=tag_google)
        return redirect(reverse('configuracao', args=[request.user]))
    else:
        return redirect(reverse('configuracao', args=[request.user]))
