from django.contrib import admin
from.models import Medicos, Pacientes, HorasMedicas

# Register your models here.


admin.site.register(Pacientes)
admin.site.register(Medicos )
admin.site.register(HorasMedicas)