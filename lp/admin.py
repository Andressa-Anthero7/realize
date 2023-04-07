from django.contrib import admin
from .models import Leads, Agendamento, Atendimento, Clientes, Perfil, Tagmeta, TagGoogle, TwilioAccountSid, TwilioAuthToken

# Register your models here.

admin.site.register(Leads)
admin.site.register(Agendamento)
admin.site.register(Atendimento)
admin.site.register(Clientes)
admin.site.register(Perfil)
admin.site.register(Tagmeta)
admin.site.register(TagGoogle)
admin.site.register(TwilioAccountSid)
admin.site.register(TwilioAuthToken)

