from django.shortcuts import render
from datetime import datetime
from .models import Leads


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
    leads = Leads.objects.all()
    return render(request, 'site/dashboard.html', {'leads': leads})
