from django.db import models

# Create your models here.
class Paciente(models.Model):
    """
        Paciente:
        - Nombre.
        - Apellido.
        - Documento.
        - Numero.
    """
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=100,
        blank=False, null=False
    )
    apellido = models.CharField(
        verbose_name='Apellidos',
        max_length=100,
        blank=False, null=False
    )
    documento = models.CharField(
        verbose_name='Tipo de Documento',
        max_length=100,
        blank=False, null=False
    )
    numero = models.CharField(
        verbose_name='Numero de Documento',
        max_length=100,
        blank=False, null=False
    )
