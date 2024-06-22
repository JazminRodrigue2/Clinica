
from django.contrib.auth.models import AbstractUser
from django.db import models

# Users/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Campos adicionales como apellido_paterno, etc.
    nombre = models.CharField(max_length=100, blank=True)
    apellido_paterno = models.CharField(max_length=100, blank=True)
    apellido_materno = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Cambia 'customuser_set' por el nombre que prefieras
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username
