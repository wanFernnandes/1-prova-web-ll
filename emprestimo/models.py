# models.py
from django.conf import settings
from django.db import models
from gerencialivro.models import Livro
from django.utils import timezone


class Alocacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livro} alocado para {self.usuario}"

    def finalizar_alocacao(self):
        """Marca o empréstimo como concluído e registra a data de devolução."""
        self.data_fim = timezone.now().date()
        self.ativo = False
        self.save()
