from django.db import models
from app.company.models import Empleado

# Create your models here.


class Registro(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    inicio = models.TimeField(verbose_name='Entrada')
    fin = models.TimeField(verbose_name='Salida', blank=True, null=True)
    horas = models.SmallIntegerField(
        verbose_name='Horas', blank=True, null=True)
    minutos = models.SmallIntegerField(
        verbose_name='Horas',  blank=True, null=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, related_name='registros')

    def __str__(self):
        return str(self.fecha) + ' ' + str(self.inicio)
