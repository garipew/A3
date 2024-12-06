from django.db import models
from produto.models import Camiseta
from django.contrib.auth.models import User

# Create your models here.

class PedidoItem(models.Model):
	camiseta = models.ForeignKey(Camiseta, on_delete=models.CASCADE)
	quantidade = models.PositiveIntegerField(default=1)	
	def calcular_preco(self):
		return self.camiseta.preco * self.quantidade
	def __str__(self):
		return self.camiseta.nome + ' ' + str(self.quantidade)

class Pedido(models.Model):
	dono = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=25, default='Em analise')
	itens = models.ManyToManyField(PedidoItem, related_name="itens")
	def calcular_preco(self):
		return sum(i.calcular_preco() for i in self.itens.all())
     
