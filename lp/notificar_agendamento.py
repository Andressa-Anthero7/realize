from celery import shared_task
from datetime import datetime, timedelta
from twilio.rest import Client
import time


@shared_task
def notificar_agenda(data_evento, account_sid, auth_token, nome_agendamento, atendimento_vinculado):
    # Timedelta function demonstration

    ano = int(data_evento[:4])
    mes = int(data_evento[5:7])
    dia = int(data_evento[8:10])
    hora = int(data_evento[11:13])
    minuto = int(data_evento[14:16])
    evento = datetime(ano, mes, dia, hour=hora, minute=minuto, second=0, microsecond=0)
    notificacao = evento - \
                       timedelta(minutes=3)
    print(evento)
    agora = datetime.now()
    calculo = notificacao - agora
    calculo = calculo / timedelta(seconds=1)
    print(calculo)

    time.sleep(calculo)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você tem um agendamento dia {data_evento[8:10]}/{data_evento[5:7]}/{data_evento[:4]} ás {data_evento[11:13]}h{data_evento[14:16]} com {nome_agendamento}\n Acesse atendimento em http://nix2022.pythonanywhere.com/atendimento/{atendimento_vinculado}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)
