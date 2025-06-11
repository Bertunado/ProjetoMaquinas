from django.db import models
from django.contrib.auth.models import User

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    maquina = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='pecas/')
    categoria = models.CharField(max_length=100) 
    data_adicao = models.DateTimeField(auto_now_add=True)
    adicionada_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    adicionada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"