#Importa o módulo admin do Django, que contém todas as ferramentas para configurar o painel de administração.
from django.contrib import admin

#mporta o modelo Cliente da aplicação atual (representado por .) para que ele possa ser registrado no admin.
from .models import Cliente

#Esse comando registra o modelo e no site de administração do Django, o que faz com que ele apareça na interface administrativa.
admin.site.register(Cliente)