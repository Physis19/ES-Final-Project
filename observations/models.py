from django.db import models
from labs.models import Laboratorio
from django.contrib.auth.models import User

class Observacao(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='observacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Texto da Observação")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"Observação de {self.usuario} em {self.laboratorio}"
