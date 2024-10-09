from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100, default='1234')  # Adicione o padrão aqui

    def __str__(self):
        return self.nome+" - "+self.cpf+ " - " +self.email
