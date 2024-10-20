from django.db import models

class Livro(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    id_livros = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.autor} - {self.id_livros} - {self.titulo} - {self.ano}'

