from pyexpat import model
from app import attendance
from app.attendance.models import Registro
from app.company.models import Empleado
from rest_framework import serializers


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ['fecha', 'inicio', 'fin', 'horas', 'minutos']


class EmpleadoSerializer(serializers.ModelSerializer):
    #registros = serializers.StringRelatedField(many=True)

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellidos']  # , 'registros']


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['fecha', 'inicio', 'fin', 'horas', 'minutos']
