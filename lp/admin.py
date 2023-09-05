from django.contrib import admin
from .models import Leads, LandingPage, Perfil, Tagmeta, TagGoogle, ItensDestaque, Cores

# Register your models here.

admin.site.register(Leads)
admin.site.register(LandingPage)
admin.site.register(Perfil)
admin.site.register(Tagmeta)
admin.site.register(TagGoogle)
admin.site.register(ItensDestaque)
admin.site.register(Cores)

