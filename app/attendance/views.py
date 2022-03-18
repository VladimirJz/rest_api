from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from app.attendance.models import Registro
from app.company.models import Empleado
from app.attendance.serializers import RegistroSerializer, EmpleadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all().order_by('-inicio')
    serializer_class = RegistroSerializer
    #permission_classes = [permissions.IsAuthenticated]


class RegistroList(APIView):
    def get(self, request, format=None):
        registros = Registro.objects.all()
        serializer = RegistroSerializer(registros, many=True)
        return Response(serializer.data)


class EmpleadosList(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class RegistroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
