
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from Users.models import CustomUser
from rest_framework import generics, permissions
from rest_framework.response import Response
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer
from django.contrib.auth.models import Group
from rest_framework import generics, permissions
from rest_framework.response import Response
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def LoginView(request):
    context = {}
    return render(request,'login.html', context)


class CustomAuthToken(ObtainAuthToken):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        # Determine the group of the user
        if user.groups.filter(name='admin_group').exists():
            redirect_url = '/admin_group/'
            print(redirect_url)
        elif user.groups.filter(name='paciente_group').exists():
            redirect_url = '/paciente_group/'
        else:
            redirect_url = '/ruta_template_default/'

        return Response({'token': token.key, 'redirect_url': redirect_url})


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class AdminTemplateView(TemplateView):
    template_name = 'admin_template.html'

class PacienteTemplateView(TemplateView):
    template_name = 'paciente_template.html'

class PacienteListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.filter(groups__name='paciente_group')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes realizar cualquier lógica adicional antes de guardar el usuario
        serializer.save()

class PacienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(groups__name='paciente_group')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Aquí puedes realizar cualquier lógica adicional antes de actualizar el usuario
        serializer.save()

    def perform_destroy(self, instance):
        # Aquí puedes realizar cualquier lógica adicional antes de eliminar el usuario
        instance.delete()


@csrf_exempt
def logout(request):
    django_logout(request)
    return redirect('/')  # Redirige a la página de inicio de sesión después de cerrar sesión
