from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Informacao(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=100)
    resposta = models.TextField()

    def __str__(self):
        return self.titulo