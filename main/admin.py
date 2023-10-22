from django.contrib import admin


# Register your models here.
from .models import Acciones, RegistroCO, Configuracion

admin.site.register(Acciones)
admin.site.register(RegistroCO)
admin.site.register(Configuracion)