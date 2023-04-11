def notificar_agenda(data_evento, account_sid, auth_token, nome_agendamento, atendimento_vinculado):
    # Timedelta function demonstration
    from datetime import datetime, timedelta, time
    from twilio.rest import Client
    ano = int(data_evento[:4])
    mes = int(data_evento[5:7])
    dia = int(data_evento[8:10])
    hora = int(data_evento[11:13])
    minuto = int(data_evento[14:16])
    evento = datetime(ano, mes, dia, hour=hora, minute=minuto, second=0, microsecond=0)
    agendamento = evento - \
                  timedelta(minutes=10)
    print(agendamento)

    while True:
        agora = datetime.now()
        #print(data_evento)

        #print('agora', agora)
        #print('agendamento', agendamento)
        #print(type(data_evento))

        if agora > agendamento:
            client = Client(account_sid, auth_token)
            print(client)

            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=f''' Você tem um agendamento dia {data_evento[8:10]}/{data_evento[5:7]}/{data_evento[:4]} ás {data_evento[11:13]}h{data_evento[14:16]} com {nome_agendamento}\n Acesse atendimento em http://nix2022.pythonanywhere.com/atendimento/{atendimento_vinculado}/''',
                to='whatsapp:+5516993379492'
            )

            print(message.sid)
            break
