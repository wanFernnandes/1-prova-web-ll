# urls.py
from django.urls import path
from . import views

urlpatterns = [
# Exemplo de URL com o nome correto do parâmetro

    path('nova/<int:livro_id>/', views.nova_alocacao, name='nova_alocacao'),
    path('lista/', views.lista_alocacoes, name='lista_alocacoes'),
    path('finalizar/<int:id>/', views.finalizar_alocacao, name='finalizar_alocacao'),
    path('exportar_pdf/', views.exportar_alocacoes_pdf, name='exportar_alocacoes_pdf'),  # Adicione esta linha

]
