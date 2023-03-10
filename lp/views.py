from django.shortcuts import render, redirect
from datetime import datetime
from .models import Leads, Agendamento, Atendimento, Clientes


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
        return render(request, 'site/index.html')
    else:
        return render(request, 'site/index.html')


def abrirleads(request, pk):
    status_aberto = 'fa-envelope-open'
    Leads.objects.filter(pk=pk).update(status_aberto=status_aberto)


def dashboard(request):
    leads = Leads.objects.all().order_by('-data_recebimento')

    print(leads)
    return render(request, 'site/dashboard-v3.html', {'leads': leads})


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
        status_leads = request.POST.get('status_leads')
        print(status_leads)
        Leads.objects.filter(pk=pk).update(status_leads=status_leads)


def criar_agendamento(request):
    if request.method == 'POST':
        nome_agendamento = request.POST.get('nome_agendamento')
        data_evento = request.POST.get('data_evento')
        data_termino = request.POST.get('data_termino')
        print(data_termino)
        data_agendamento = datetime.now()
        user_agendamento = request.user
        Agendamento.objects.create(
            nome_agendamento=nome_agendamento,
            data_evento=data_evento,
            data_termino=data_termino,
            data_agendamento=data_agendamento,
            user_agendamento=user_agendamento,
        )

        return render(request, 'site/atendimento.html')
    else:
        return render(request, 'site/atendimento.html')


def criar_atendimento(request):
    if request.method == 'POST':
        print('anotacoes_atendimento')
        anotacoes_atendimento = request.POST.get('anotacoes')

        atendimento_vinculado = request.POST.get('id_atendimento')
        data_inclusao_atendimento = datetime.now()
        user_logado_inclusao = request.user

        Atendimento.objects.create(
            anotacoes_atendimento=anotacoes_atendimento,
            atendimento_vinculado=atendimento_vinculado,
            data_inclusao_atendimento=data_inclusao_atendimento,
            user_inclusao_atendimento=user_logado_inclusao,

        )

        return redirect('atendimento', pk=atendimento_vinculado)
    else:
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
