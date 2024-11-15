from django import forms
from .models import Alocacao
class AlocacaoForm(forms.ModelForm):
    class Meta:
        model = Alocacao
        fields = ['livro', 'usuario', 'data_inicio', 'data_fim', 'ativo']

