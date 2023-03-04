from django.shortcuts import render
from datetime import datetime
from .models import Leads, Agendamento


# Create your views here.


def index(request):
    if request.method == 'POST':
        nome_leads = request.POST.get('nome')
        email_leads = request.POST.get('email')
        whatsapp_leads = request.POST.get('whatsapp')
        status_aberto = 'NÃO'
        data_recebimento = datetime.now()
        Leads.objects.create(nome_leads=nome_leads,
                             email=email_leads,
                             whatsapp=whatsapp_leads,
                             status_aberto=status_aberto,
                             data_recebimento=data_recebimento)
        return render(request, 'site/index.html')
    else:
        return render(request, 'site/index.html')


def dashboard(request):
    leads = Leads.objects.all().order_by('-data_recebimento')

    print(leads)
    return render(request, 'site/dashboard-v3.html', {'leads': leads})


def atendimento(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'site/atendimento.html', {'agendamentos': agendamentos})


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
