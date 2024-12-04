from django.contrib import admin
from AppRiver.models import Socio, Actividad, EntradasTorneoLocal,EntradasCopa
# Register your models here.
admin.site.register(Socio)
admin.site.register(Actividad)
admin.site.register(EntradasTorneoLocal)
admin.site.register(EntradasCopa)