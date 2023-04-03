def notificacao(leads_pk):
    from twilio.rest import Client
    from django.conf import settings

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você recebeu um Leads.\nAcesse em https://nix2022.pythonanywhere.com/atendimento/{leads_pk}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)
