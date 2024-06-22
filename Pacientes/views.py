# Users/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer
from django.contrib.auth.models import Group

class PacienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(groups__name='paciente')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes realizar cualquier lógica adicional antes de guardar el usuario
        serializer.save()

class PacienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(groups__name='paciente')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Aquí puedes realizar cualquier lógica adicional antes de actualizar el usuario
        serializer.save()

    def perform_destroy(self, instance):
        # Aquí puedes realizar cualquier lógica adicional antes de eliminar el usuario
        instance.delete()
