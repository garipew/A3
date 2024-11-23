from django.db import models

# Create your models here.
class Camiseta(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.URLField()
    descricao = models.TextField(blank=True)
    def __str__(self):
        return self.nome
