from django.contrib import admin
from app.company.models import Empresa, Departamento, Empleado, Area

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Area)
