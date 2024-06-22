
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'email', 'groups', 'password')
