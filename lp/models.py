from django.db import models


# Create your models here.

class Leads(models.Model):
    STATUS_LEITURA = (
        ('LIDO', 'LIDO'),
        ('NOVO', 'NOVO'),
    )

    STATUS_LEADS = (
        ('FORTE', 'FORTE'),
        ('NEUTRO', 'NEUTRO'),
        ('FRACO', 'FRACO')
    )

    nome_leads = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=11)
    status_aberto = models.CharField(max_length=4, choices=STATUS_LEITURA)
    status_leads = models.CharField(max_length=6, choices=STATUS_LEADS)
    data_recebimento = models.CharField(max_length=50)
    ultimo_user = models.CharField(max_length=30)


class Agendamento(models.Model):
    nome_agendamento = models.CharField(max_length=30)
    data_evento = models.CharField(max_length=50)
    data_termino = models.CharField(max_length=50)
    data_agendamento = models.CharField(max_length=50)
    user_agendamento = models.CharField(max_length=50)