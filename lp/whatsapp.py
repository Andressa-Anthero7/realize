def notificacao(leads_pk, account_sid,  auth_token):
    from twilio.rest import Client
    from django.conf import settings

<<<<<<< HEAD
    client = Client(account_sid, auth_token)
=======
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    print(client)
>>>>>>> 616ad19024f37932e230dd745ef940f904aa8985

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você recebeu um Leads.\nAcesse em http://nix2022.pythonanywhere.com/atendimento/{leads_pk}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)
