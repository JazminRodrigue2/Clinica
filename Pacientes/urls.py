# Users/urls.py

from django.urls import path
from .views import PacienteListCreateAPIView, PacienteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('pacientes/', PacienteListCreateAPIView.as_view(), name='paciente_list_create'),
    path('pacientes/<int:pk>/', PacienteRetrieveUpdateDestroyAPIView.as_view(), name='paciente_retrieve_update_destroy'),
    # Agrega otras URLs según sea necesario para tu aplicación
]
