from django.db import models
from produto.models import Camiseta

# Create your models here.

class CarrinhoItem(models.Model):
    # Um único item do carrinho
    camiseta = models.ForeignKey(Camiseta, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    def calcular_preco(self):
        return self.camiseta.preco * self.quantidade

    def __str__(self):
        return self.camiseta.nome + ' ' + str(self.quantidade)

class Carrinho(models.Model):
    # O carrinho como um todo
    sessao = models.CharField(max_length=40, unique=True)
    itens = models.ManyToManyField(CarrinhoItem, related_name="itens")
    def calcular_preco(self):
        return sum(i.calcular_preco for i in self.itens.all())
     
