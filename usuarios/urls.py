from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('deletar/<int:pk>/', views.deletar_usuarios, name='deletar_usuarios'),
    path('atualizar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),
    #path('login/', views.login_usuario, name='login_usuario'),
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('exportar_usuario_pdf/', views.usuario_pdf, name='usuario_pdf'),  # Adicione esta linha
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login_usuario.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


   
]
