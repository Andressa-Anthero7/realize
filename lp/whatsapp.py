from twilio.rest import Client


def notificacao(leads_pk, account_sid, auth_token):
    client = Client(account_sid, auth_token)
    print(client)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você recebeu um Leads.\nAcesse em http://nix2022.pythonanywhere.com/atendimento/{leads_pk}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)


