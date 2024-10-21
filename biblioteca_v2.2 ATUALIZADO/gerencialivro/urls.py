from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/novo/', views.criar_livros, name='criar_livros'),
    path('livros/atualizar/<int:id>/', views.atualizar_livros, name='atualizar_livros'),
    path('livros/deletar/<int:id>/', views.deletar_livros, name='deletar_livros'),
    path('livros/exportar_pdf/', views.exportar_livros_pdf, name='exportar_livros_pdf'),
    
]


