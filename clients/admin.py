from django.contrib import admin

from clients.models import Paciente

# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass