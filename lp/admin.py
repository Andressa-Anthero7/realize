from django.contrib import admin
from .models import Leads, Agendamento, Atendimento, Clientes, Perfil, Tagmeta

# Register your models here.

admin.site.register(Leads)
admin.site.register(Agendamento)
admin.site.register(Atendimento)
admin.site.register(Clientes)
admin.site.register(Perfil)
admin.site.register(Tagmeta)
