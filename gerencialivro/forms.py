from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['id_livros', 'autor', 'titulo', 'ano', 'genero']
