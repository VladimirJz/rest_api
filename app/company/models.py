from django.db import models
from django.db.models import TextField

# Create your models here.


class Empresa(models.Model):
    nombre_empresa = models.TextField(max_length=30, verbose_name='Empresa')

    def __str__(self):
        return self.nombre_empresa


class Oficina(models.Model):
    nombre_oficina = models.TextField(max_length=30, verbose_name='Oficina')
    direccion = models.TextField(max_length=300, verbose_name='Direccion')

    def __str__(self):
        return self.nombre_oficina


class Area(models.Model):
    nombre_area = models.TextField(max_length=30, verbose_name='Area')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_area


class Departamento(models.Model):
    nombre_departamento = models.TextField(
        max_length=30, verbose_name='Departamento')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_departamento


class Empleado(models.Model):
    nombre = models.TextField(max_length=30, verbose_name='Nombre')
    apellidos = models.TextField(max_length=30, verbose_name='Apellidos')
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre + self.apellidos
