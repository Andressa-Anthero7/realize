def notificacao(leads_pk):
    from twilio.rest import Client
    print(leads_pk)
    account_sid = 'AC95d4a3b7262a74d20f1f52f3ac588308'
    auth_token = '0e4f4b19f105062e11d500601e720485'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f''' Você recebeu um Leads.\nAcesse em https://nix2022.pythonanywhere.com/atendimento/{leads_pk}/''',
        to='whatsapp:+5516993379492'
    )

    print(message.sid)