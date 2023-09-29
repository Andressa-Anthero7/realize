from django.contrib import admin
from .models import Leads, LandingPage, Perfil, Tagmeta, TagGoogle, Cores, TagGoogleBody,\
    ItensOpcioanis, QtdeQuartos, Qtdesuites, QtdeVagaGaragem

# Register your models here.

admin.site.register(Leads)
admin.site.register(LandingPage)
admin.site.register(Perfil)
admin.site.register(Tagmeta)
admin.site.register(TagGoogle)
admin.site.register(TagGoogleBody)
admin.site.register(Cores)
admin.site.register(ItensOpcioanis)
admin.site.register(QtdeQuartos)
admin.site.register(Qtdesuites)
admin.site.register(QtdeVagaGaragem)



