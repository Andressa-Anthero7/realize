def notificacao(leads_pk):
    from twilio.rest import Client

    account_sid = 'ACc4b4a408cd71392b6e1240e43319dade'
    auth_token = '1a3b0a6f090dbf09b67884ce75b6d966'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você recebeu um Leads.\nAcesse em https://nix2022.pythonanywhere.com/atendimento/{leads_pk}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)

