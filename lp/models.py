from django.db import models


# Create your models here.

class Leads(models.Model):
    STATUS_LEADS = (
        ('FORTE', 'FORTE'),
        ('NEUTRO', 'NEUTRO'),
        ('FRACO', 'FRACO')
    )

    nome_leads = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=11)
    status_aberto = models.CharField(max_length=4)
    status_leads = models.CharField(max_length=6, choices=STATUS_LEADS)
    data_recebimento = models.CharField(max_length=50)
    ultimo_user = models.CharField(max_length=30)


class Agendamento(models.Model):
    nome_agendamento = models.CharField(max_length=30)
    data_evento = models.CharField(max_length=50)
    data_termino = models.CharField(max_length=50)
    data_agendamento = models.CharField(max_length=50)
    user_agendamento = models.CharField(max_length=50)


class Atendimento(models.Model):
    leads_atendimento = models.CharField(max_length=10, primary_key=True)
    anotacoes_atendimento = models.TextField(max_length=300)
    data_inclusao_atendimento = models.CharField(max_length=15)
    user_inclusao_atendimento = models.CharField(max_length=50)


class Clientes(models.Model):
    atendimento_vinculados_cliente = models.CharField(max_length=10, primary_key=True)
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.CharField(max_length=100)
    whatsapp_cliente = models.CharField(max_length=14)
    cnpj_cpf_cliente = models.CharField(max_length=14)
    endereco_cliente = models.CharField(max_length=100)
    tel_fixo_cliente = models.CharField(max_length=13)
    info_complementares = models.TextField(max_length=300)
    data_inclusao_cliente = models.CharField(max_length=15)
    user_inclusao_cliente = models.CharField(max_length=50)
