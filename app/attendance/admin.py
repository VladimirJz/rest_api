from atexit import register
from django.contrib import admin

from app.attendance.models import Registro

# Register your models here.
admin.site.register(Registro)
