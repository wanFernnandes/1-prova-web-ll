from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name="lista_clientes"),  # Adicione a barra final
    path('clientes/novo/', views.criar_cliente, name="criar_clientes"),  # Adicione a barra final
    path('clientes/editar/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('clientes/deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
    path('clientes/exportar_cliente_pdf/', views.exportar_cliente_pdf, name='exportar_cliente_pdf'),
]
