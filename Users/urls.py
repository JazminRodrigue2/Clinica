from django.urls import path
from .views import CustomAuthToken, UserDetail, LoginView, AdminTemplateView, PacienteListCreateAPIView, PacienteRetrieveUpdateDestroyAPIView, logout, PacienteTemplateView

urlpatterns = [
    path('', LoginView, name="login_view"),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('user-detail/', UserDetail.as_view(), name='user_detail'),
    
    path('admin_group/', AdminTemplateView.as_view(), name='admin_group'),
    path('admin_group/pacientes/', PacienteListCreateAPIView.as_view(), name='paciente_list_create'),
    path('admin_group/pacientes/<int:pk>/', PacienteRetrieveUpdateDestroyAPIView.as_view(), name='paciente_retrieve_update_destroy'),
    
    path('paciente/', PacienteTemplateView.as_view(), name='paciente_group'),
    
    path('logout/', logout, name='logout'),

]
