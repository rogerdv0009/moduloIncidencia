from django.contrib import admin
from .models import Incidencia
# Register your models here.

#class IncidenciaAdmin(admin.ModelAdmin):
 #   readonly_fields=('fecha_creado')
admin.site.register(Incidencia)

